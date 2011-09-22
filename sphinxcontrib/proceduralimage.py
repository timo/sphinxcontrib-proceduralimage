from docutils import nodes

import posixpath
from os import path

try:
    from hashlib import sha1 as sha
except ImportError:
    from sha import sha

from sphinx.errors import SphinxError
from sphinx.util.compat import Directive
from sphinx.util import ensuredir


class ProceduralimageError(SphinxError):
    category = 'Proceduralimage error'

class proceduralimage(nodes.General, nodes.Element):
    pass

class Proceduralimage(Directive):
    """
    Directive to insert python code, that generates an image.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
    }

    def run(self):
        pycode = '\n'.join(self.content)
        if not pycode.strip():
            return [self.state_machine.reporter.warning(
                'Ignoring "proceduralimage" directive without content.',
                line=self.lineno)]
        node = proceduralimage()
        node['code'] = pycode
        node['options'] = []
        return [node]

def render_proceduralimage(self, code, options):
    mylocals = dict(alt=None)
    mylocals["image_data"] = None
    mylocals["alt"] = None

    exec code in mylocals, mylocals

    return mylocals["image_data"], mylocals["alt"]

def render_proceduralimage_html(self, node, code, options, prefix='proceduralimage',
                    imgcls=None, alt=None):

    # if the image has already been made, take it from the cache
    hashkey = code.encode('utf-8') + str(options)
    fname = '%s-%s.%s' % (prefix, sha(hashkey).hexdigest(), "png")

    relfn = posixpath.join(self.builder.imgpath, fname)
    outfn = path.join(self.builder.outdir, '_images', fname)

    if not path.isfile(outfn):

        try:
            image_data, alt = render_proceduralimage(self, code, options)
        except ProceduralimageError, exc:
            self.builder.warn('proceduralimage code %r: ' % code + str(exc))
            raise nodes.SkipNode

        if image_data is None:
            relfn = None
        else:
            ensuredir(path.dirname(outfn))
            with open(outfn, "w") as outfile:
                outfile.write(image_data)
            with open(outfn + ".alt.txt", "w") as altfile:
                altfile.write(alt)

    else:
        with open(outfn + ".alt.txt", "r") as altfile:
            alt = altfile.read()
        if not alt:
            alt = None

    self.body.append(self.starttag(node, 'p', CLASS='proceduralimage'))
    if relfn is None:
        self.body.append(self.encode(code))
    else:
        self.body.append('<img src="%s" alt="%s"/>\n' %
                         (relfn, alt))

    self.body.append('</p>\n')
    raise nodes.SkipNode

def html_visit_proceduralimage(self, node):
    render_proceduralimage_html(self, node, node['code'], node['options'])

def setup(app):
    app.add_node(proceduralimage,
                 html=(html_visit_proceduralimage, None))
    app.add_directive('proceduralimage', Proceduralimage)

