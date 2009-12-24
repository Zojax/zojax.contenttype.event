##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" event implementation

$Id$
"""
from zope import interface, component
from zope.proxy import removeAllProxies
from zope.schema.fieldproperty import FieldProperty
from zope.cachedescriptors.property import Lazy
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zojax.richtext.field import RichTextProperty
from zojax.content.type.item import PersistentItem
from zojax.content.type.searchable import ContentSearchableText

from interfaces import IEvent


class Event(PersistentItem):
    interface.implements(IEvent)

    text = RichTextProperty(IEvent['text'])
    endDate = FieldProperty(IEvent['endDate'])
    startDate = FieldProperty(IEvent['startDate'])


class SearchableText(ContentSearchableText):
    component.adapts(IEvent)

    def getSearchableText(self):
        text = super(SearchableText, self).getSearchableText()

        try:
            return text + u' ' + self.content.text.text
        except AttributeError:
            return text
