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
""" event interfaces

$Id$
"""
from zope import schema, interface
from z3c.schema.baseurl import BaseURL
from z3c.schema.email import RFC822MailAddress
from zojax.widget.list import SimpleList
from zojax.richtext.field import RichText
from zojax.contenttypes.interfaces import _
from zojax.calendar.interfaces import IEvent, IEventLocation


class IEvent(IEvent, IEventLocation):

    attendees = SimpleList(
        title = _(u'Attendees'),
        value_type = schema.TextLine(),
        required = False)

    eventUrl = BaseURL(
        title = _(u'Event URL'),
        description = _(u'Web address with more info about the event.'),
        required = False)

    contactName = schema.TextLine(
        title = _(u'Contact Name'),
        required = False)

    contactEmail = RFC822MailAddress(
        title = _(u'Contact E-mail'),
        required = False)

    contactPhone = schema.TextLine(
        title = _(u'Contact Phone'),
        required = False)

    text = RichText(
        title = _(u'Body'),
        description = _(u'Event body text.'),
        required = False)

    cooked_text = interface.Attribute('Cooked text')


class IEventType(interface.Interface):
    """ event content type """
