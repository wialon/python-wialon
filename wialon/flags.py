#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base item information
ITEM_DATAFLAG_BASE = 0x00000001
# Item custom properties
ITEM_DATAFLAG_CUSTOM_PROPS = 0x00000002
# Item billing/construction properties
ITEM_DATAFLAG_BILLING_PROPS = 0x00000004
# Item custom fields
ITEM_DATAFLAG_CUSTOM_FIELDS = 0x00000008
# Item image 
ITEM_DATAFLAG_IMAGE = 0x00000010
# Item messages
ITEM_DATAFLAG_MESSAGES = 0x00000020
# Item GUID
ITEM_DATAFLAG_GUID = 0x00000040
# Admin fields plugin
ITEM_DATAFLAG_ADMINFIELDS = 0x00000080

# User has at least view access to given item
ITEM_ACCESSFLAG_VIEW = 0x1
# User can view detailed item properties
ITEM_ACCESSFLAG_VIEW_PROPERTIES = 0x2
# User can update ACL settings for item or user
ITEM_ACCESSFLAG_SET_ACL = 0x4
# User can delete item
ITEM_ACCESSFLAG_DELETE_ITEM = 0x8
# User can change item name
ITEM_ACCESSFLAG_EDIT_NAME = 0x10
# view custom fields
ITEM_ACCESSFLAG_VIEW_CFIELDS = 0x20
# create, edit and delete custom fields
ITEM_ACCESSFLAG_EDIT_CFIELDS = 0x40
# edit other item settings, not mentioned with own mask
ITEM_ACCESSFLAG_EDIT_OTHER = 0x80
# edit item image
ITEM_ACCESSFLAG_EDIT_IMAGE = 0x100
# execute reports over item, incl. raw messages access
ITEM_ACCESSFLAG_EXEC_REPORTS = 0x200
# edit ACL-propagated items, e.g. edit units in units group
ITEM_ACCESSFLAG_EDIT_SUBITEMS = 0x400
# view, add and delete item log records
ITEM_ACCESSFLAG_MANAGE_LOG = 0x800
# view admin fields
ITEM_ACCESSFLAG_VIEW_ADMINFIELDS = 0x1000
# create, edit and delete admin fields
ITEM_ACCESSFLAG_EDIT_ADMINFIELDS = 0x2000

# AVL message flags mask determining message type
ITEM_MESSAGEFLAG_TYPE_MASK = 0xFF00
# AVL message flag, set when message represents data sent from unit
ITEM_MESSAGEFLAG_TYPE_UNIT_DATA = 0x0000
# AVL message flag, set when message represents incoming SMS
ITEM_MESSAGEFLAG_TYPE_UNIT_SMS = 0x0100
# AVL message flag, set when message represents command over unit
ITEM_MESSAGEFLAG_TYPE_UNIT_CMD = 0x0200
#  AVL message flag, set when message represents event
ITEM_MESSAGEFLAG_TYPE_UNIT_EVENT = 0x0600
# Storage message flag, set when message represents log of user actions
ITEM_MESSAGEFLAG_TYPE_USER_LOG = 0x0400
# AVL message flag, set when message type is user notification
ITEM_MESSAGEFLAG_TYPE_NOTIFICATION = 0x0300
# Billing message flag, set when message represents billing balance update
ITEM_MESSAGEFLAG_TYPE_BALANCE = 0x0500
# Storage message flag, set when message represents plot cultivation
ITEM_MESSAGEFLAG_TYPE_AGRO_CULTIVATION = 0x0700
# AVL message type, set when message type is SMS from driver
ITEM_MESSAGEFLAG_TYPE_DRIVER_SMS = 0x0900
# AVL message flag, set when represents unit log messages
ITEM_MESSAGEFLAG_TYPE_LOG_RECORD = 0x1000
# AVL message flag, set when message type is something different
ITEM_MESSAGEFLAG_TYPE_OTHER = 0xFF00

""" Data flags constants """
# Drivers plugin
ITEM_RESOURCE_DATAFLAG_DRIVERS = 0x00000100
# Jobs plugin
ITEM_RESOURCE_DATAFLAG_JOBS = 0x00000200
# POI plugin
ITEM_RESOURCE_DATAFLAG_POI = 0x00000800
# Notifications plugin
ITEM_RESOURCE_DATAFLAG_NOTIFICATIONS = 0x00000400
# Geofences plugin
ITEM_RESOURCE_DATAFLAG_ZONES = 0x00001000
# Reports plugin
ITEM_RESOURCE_DATAFLAG_REPORTS = 0x00002000
# Agro plugins
ITEM_RESOURCE_DATAFLAG_AGRO = 0x01000000
# Driver units
ITEM_RESOURCE_DATAFLAG_DRIVER_UNITS = 0x00004000
# Driver groups plugin
ITEM_RESOURCE_DATAFLAG_DRIVER_GROUPS = 0x00008000
# Trailers plugin
ITEM_RESOURCE_DATAFLAG_TRAILERS = 0x00010000
# Trailer groups plugin
ITEM_RESOURCE_DATAFLAG_TRAILER_GROUPS = 0x00020000
# Trailer units
ITEM_RESOURCE_DATAFLAG_TRAILER_UNITS = 0x00040000

""" Unit dataflgs """
# Unit restricted props
ITEM_UNIT_DATAFLAG_RESTRICTED = 0x00000100
# Unit commands
ITEM_UNIT_DATAFLAG_COMMANDS = 0x00000200
# Unit commands aliases
ITEM_UNIT_DATAFLAG_COMMAND_ALIASES = 0x00080000
# TODO

""" User flags """
#
ITEM_USER_USERFLAG_CAN_CREATE_ITEMS = 0x00000004
# TODO

""" Item ACL flags """
# User has at least view access to given item
ITEM_ACCESSFLAG_VIEW = 0x1

""" Resource ACL flags """
# View notification
ITEM_RESOURCE_ACCESSFLAG_VIEW_NOTIFICATION = 0x100000
# Create, edit and delete notification
ITEM_RESOURCE_ACCEESSFLAG_EDIT_NOTIFICATION = 0x200000
# View jobs
ITEM_RESOURCE_ACCEESSFLAG_VIEW_JOBS = 0x4000000
# Edit jobs
ITEM_RESOURCE_ACCEESSFLAG_EDIT_JOBS = 0x8000000
# View POI
ITEM_RESOURCE_ACCEESSFLAG_VIEW_POI = 0x400000
# Edit POI
ITEM_RESOURCE_ACCEESSFLAG_EDIT_POI = 0x800000
# View geozones
ITEM_RESOURCE_ACCEESSFLAG_VIEW_ZONES = 0x1000000
# Edit geozones
ITEM_RESOURCE_ACCEESSFLAG_EDIT_ZONES = 0x2000000
# View reports
ITEM_RESOURCE_ACCEESSFLAG_VIEW_REPORTS = 0x10000000

""" Unit ACL flags """
# View, edit connectivity settings: HW, UID, Phone, Password, input-message-filter
ITEM_UNIT_ACCESSFLAG_EDIT_DEVICE = 0x100000
# Execute commands over unit
ITEM_UNIT_ACCESSFLAG_EXECUTE_COMMANDS = 0x1000000
# View command aliases
ITEM_UNIT_ACCESSFLAG_VIEW_COMMAND_ALIASES = 0x400000000
# Include unit in various auto-processing systems like retranslation, jobs, notifications
ITEM_UNIT_ACCESSFLAG_MONITOR_STATE = 0x8000000000
# Register various unit events, store counters, bind/unbind drivers and change unit status
ITEM_UNIT_ACCESSFLAG_REGISTER_EVENTS = 0x2000000
