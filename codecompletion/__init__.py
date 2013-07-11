# -*- coding: utf-8 -*-

# gEdit CodeCompletion plugin
# Copyright (C) 2011 Fabio Zendhi Nagao
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import GObject, Gtk, Gedit

class CodeCompletionWindowActivateable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__  = "CodeCompletionWindowActivateable"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self.provider = jsonprovider.JSONProvider(self)

        # Add the provider to all the views
        for view in self.window.get_views():
            view.get_completion().add_provider(self.provider)
        
        self.tab_added_id = self.window.connect('tab-added', self.callback_on_tab_added)
        self.tab_removed_id = self.window.connect('tab-removed', self.callback_on_tab_removed)

    def do_deactivate(self):
        # Remove the provider from all the views
        for view in self.window.get_views():
            view.get_completion().remove_provider(self.provider)

        self.window.disconnect(self.tab_added_id)
        self.window.disconnect(self.tab_removed_id)

    def do_update_state(self):
        pass

    def callback_on_tab_added(self, window, tab):
        tab.get_view().get_completion().add_provider(self.provider)

    def callback_on_tab_removed(self, window, tab):
        tab.get_view().get_completion().remove_provider(self.provider)


class CodeCompletionViewActivateable(GObject.Object, Gedit.ViewActivatable):
    __gtype_name__ = "CodeCompletionViewActivateable"
    view = GObject.property(type=Gedit.View)
    window = GObject.property(type=Gedit.Window)
#    WINDOW_DATA_KEY = "JSONCompletionPluginWindowData"
    
    def __init__(self):
        GObject.Object.__init__(self)
    
    def do_activate(self):
        print ("do_activate view " + str(self.window))
        #helper = CodeCompletionWindowActivateable(self, self.window)
        #self.window.set_data(self.WINDOW_DATA_KEY, helper)
    
    def do_deactivate(self):
        print ("do_deactivate view " + str(self.window))
        #self.window.get_data(self.WINDOW_DATA_KEY).deactivate()
        #self.window.set_data(self.WINDOW_DATA_KEY, None)
    
#    def do_update_state(self, window):
#        self.window.update_ui()

# ex:ts=4:et:
