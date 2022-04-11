import qiime2.sdk
from mmvec import __version__, _heatmap_choices, _cmaps
from qiime2.plugin import (Str, Properties, Int, Float, Metadata, Bool,
        Plugin)

plugin = Plugin(
    name='mmvec',
    version=__version__,
    website="https://github.com/biocore/mmvec",
    short_description='Plugin for performing microbe-metabolite '
                      'co-occurence analysis.',
    description='This is a QIIME 2 plugin supporting microbe-metabolite '
                'co-occurence analysis using mmvec.',
    package='mmvec')

