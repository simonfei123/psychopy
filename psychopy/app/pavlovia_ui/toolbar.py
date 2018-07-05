import wx

from os.path import join
from .. import icons
from .project import syncProject
from .search import SearchFrame
from ._base import PavloviaMiniBrowser


class PavloviaButtons:

    def __init__(self, frame, toolbar, tbSize):
        self.frame = frame
        self.toolbar = toolbar
        self.tbSize = tbSize

    def addPavloviaTools(self, buttons=['sync', 'run', 'search', 'user']):
        rc = self.frame.app.prefs.paths['resources']

        info={}
        info['run'] = {'emblem': 'run16.png', 'func': self.onPavloviaRun}
        info['sync'] = {'emblem': 'sync_green16.png', 'func': self.onPavloviaSync}
        info['search'] = {'emblem': 'magnifier16.png', 'func': self.onPavloviaSearch}
        info['user'] = {'emblem': 'user22.png', 'func': self.onPavloviaUser}

        for buttonName in buttons:
            emblem = info[buttonName]['emblem']
            btnFunc = info[buttonName]['func']
            tool = self.toolbar.AddSimpleTool(
                wx.ID_ANY,
                icons.combineImageEmblem(
                    main=join(rc, 'globe%i.png' % self.tbSize),
                    emblem=join(rc, emblem), pos='bottom_right'))
            self.toolbar.Bind(wx.EVT_TOOL, btnFunc, tool)

    def onPavloviaSync(self, evt=None):
        syncProject(parent=self.frame, project=self.frame.project)

    def onPavloviaRun(self, evt=None):
        if self.project:
            self.project.pavloviaStatus = 'ACTIVATED'
            url = "https://pavlovia.org/run/{}/html".format(self.project.id)
            wx.LaunchDefaultBrowser(url)

    def onPavloviaUser(self, evt=None):
        dlg = PavloviaMiniBrowser(parent=self.frame)
        dlg.ShowModal()
        dlg.gotoUserPage()

    def onPavloviaSearch(self, evt=None):
        searchDlg = SearchFrame(
            app=self.frame.app, parent=self.frame, pos=self.frame.GetPosition())
        searchDlg.Show()
