### Access flags
## General - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#general
# View this item's basic properties
ACCESSFLAG_VIEW_ITEM_BASIC = 0x0001
# View this item's detailed properties
ACCESSFLAG_VIEW_ITEM_DETAILED = 0x0002
# Manage access to this item
ACCESSFLAG_MANAGE_ITEM_ACCESS = 0x0004
# Delete this item
ACCESSFLAG_DELETE_ITEM = 0x0008
# Rename this item
ACCESSFLAG_RENAME_ITEM = 0x0010
# View this item's custom fields
ACCESSFLAG_VIEW_CUSTOM_FIELDS = 0x0020
# Manage this item's custom fields
ACCESSFLAG_MANAGE_CUSTOM_FIELDS = 0x0040
# Manage this item's unmentioned properties
ACCESSFLAG_MANAGE_UNMENTIONED_FIELDS = 0x0080
# Manage this item's icon
ACCESSFLAG_MANAGE_ICON = 0x0100
# Query this item's reports or messages
ACCESSFLAG_QUERY_REPORTS = 0x0200
# Manage this item's ACL propagated objects
ACCESSFLAG_MANAGE_ACL = 0x0400
# Manage this item's log
ACCESSFLAG_MANAGE_ITEM_LOG = 0x0800
# View this item's administrative fields
ACCESSFLAG_VIEW_ADMIN_FIELDS = 0x1000
# Manage this item's administrative fields
ACCESSFLAG_MANAGE_ADMIN_FIELDS = 0x2000
# View this item's attached files
ACCESSFLAG_VIEW_ATTACHED_FILES = 0x4000
# Manage this item's attached files
ACCESSFLAG_MANAGE_ATTACHED_FILES = 0x8000

## Unit/Unit Group - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#units_and_unit_groups
# Manage this unit/group's connectivity settings
ACCESSFLAG_UNIT_MANAGE_CONNECTIVITY = 0x0000100000
# Manage this unit/group's sensors
ACCESSFLAG_UNIT_MANAGE_SENSORS = 0x0000200000
# Manage this unit/group's counters
ACCESSFLAG_UNIT_MANAGE_COUNTERS = 0x0000400000
# Delete this unit/group's messages
ACCESSFLAG_UNIT_DELETE_MESSAGES = 0x0000800000
# Execute this unit/group's commands
ACCESSFLAG_UNIT_EXECUTE_COMMANDS = 0x0001000000
# Register this unit/group's events
ACCESSFLAG_UNIT_REGISTER_EVENTS = 0x0002000000
# View this unit/group's connectivity settings
ACCESSFLAG_UNIT_VIEW_CONNECTIVITY = 0x0004000000
# View this unit/group's service intervals
ACCESSFLAG_UNIT_VIEW_SERVICE_INTERVALS = 0x0010000000
# Manage this unit/group's service intervals
ACCESSFLAG_UNIT_MANAGE_SERVICE_INTERVALS = 0x0020000000
# Import this unit/group's messages
ACCESSFLAG_UNIT_IMPORT_MESSAGES = 0x0040000000
# Export this unit/group's messages
ACCESSFLAG_UNIT_EXPORT_MESSAGES = 0x0080000000
# View this unit/group's commands
ACCESSFLAG_UNIT_VIEW_COMMANDS = 0x0400000000
# Manage this unit/group's commands
ACCESSFLAG_UNIT_MANAGE_COMMANDS = 0x0800000000
# Manage this unit/group's trip detector and fuel consumption
ACCESSFLAG_UNIT_MANAGE_TRIP_DETECTOR = 0x4000000000
# Manage this unit/group's job, notification, route, and retranslator assignments
ACCESSFLAG_UNIT_MANAGE_ASSIGNMENTS = 0x8000000000

## User - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#users
# Manage this user's access rights
ACCESSFLAG_USER_MANAGE_ACCESS_RIGHTS = 0x100000
# Can assume the identity of this user (login as)
ACCESSFLAG_USER_ACT_AS_OTHER = 0x200000
# Manage this user's access flags
ACCESSFLAG_USER_MANAGE_FLAGS = 0x400000
# View this user's push messages
ACCESSFLAG_USER_VIEW_PUSH_MESSAGES = 0x800000
# Manage this user's push messages
ACCESSFLAG_USER_MANAGE_PUSH_MESSAGES = 0x1000000

## Retranslator - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#retranslators
# Manage this retranslator's properties (including start/stop)
ACCESSFLAG_RETRANSLATOR_MANAGE_PROPERTIES = 0x100000
# Manage this retranslator's available units
ACCESSFLAG_RETRANSLATOR_MANAGE_UNITS = 0x2000000

## Resources (Accounts) - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#resources_accounts
# View this resource's notifications
ACCESSFLAG_RESOURCE_VIEW_NOTIFICATIONS = 0x0000000100000
# Manage this resource's notifications
ACCESSFLAG_RESOURCE_MANAGE_NOTIFICATIONS = 0x0000000200000
# View this resource's points of interest
ACCESSFLAG_RESOURCE_VIEW_POIS = 0x0000000400000
# Manage this resource's points of interest
ACCESSFLAG_RESOURCE_MANAGE_POIS = 0x0000000800000
# View this resource's geofences
ACCESSFLAG_RESOURCE_VIEW_GEOFENCES = 0x0000001000000
# Manage this resource's geofences
ACCESSFLAG_RESOURCE_MANAGE_GEOFENCES = 0x0000002000000
# View this resource's jobs
ACCESSFLAG_RESOURCE_VIEW_JOBS = 0x0000004000000
# Manage this resource's jobs
ACCESSFLAG_RESOURCE_MANAGE_JOBS = 0x0000008000000
# View this resource's report templates
ACCESSFLAG_RESOURCE_VIEW_REPORT_TEMPLATES = 0x0000010000000
# Manage this resource's report templates
ACCESSFLAG_RESOURCE_MANAGE_REPORT_TEMPLATES = 0x0000020000000
# View this resource's drivers
ACCESSFLAG_RESOURCE_VIEW_DRIVERS = 0x0000040000000
# Manage this resource's drivers
ACCESSFLAG_RESOURCE_MANAGE_DRIVERS = 0x0000080000000
# Manage this resource's account
ACCESSFLAG_RESOURCE_MANAGE_ACCOUNT = 0x0000100000000
# View this resource's orders
ACCESSFLAG_RESOURCE_VIEW_ORDERS = 0x0000200000000
# Manage this resource's orders
ACCESSFLAG_RESOURCE_MANAGE_ORDERS = 0x0000400000000
# View this resource's trailers
ACCESSFLAG_RESOURCE_VIEW_TRAILERS = 0x0100000000000
# Manage this resource's trailers
ACCESSFLAG_RESOURCE_MANAGE_TRAILERS = 0x0200000000000

## Routes - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#routes
# Manage this route's properties
ACCESSFLAG_ROUTE_MANAGE_ROUTE = 0x0000000100000

## Other - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/core/check_items_billing#other
# Sets all possible access flags to an item
ACCESSFLAG_FULL_ACCESS = 0xfffffffffffffff

### Data flags
## Resource (Accounts) - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/resource
# This resource's basic properties
DATAFLAG_RESOURCE_BASE = 0x00000001
# This resource's custom properties
DATAFLAG_RESOURCE_CUSTOM_PROPERTIES = 0x00000002
# This resource's billing properties
DATAFLAG_RESOURCE_BILLING_PROPERTIES = 0x00000004
# This resource's custom fields
DATAFLAG_RESOURCE_CUSTOM_FIELDS = 0x00000008
# This resource's messages
DATAFLAG_RESOURCE_MESSAGES = 0x00000020
# This resource's GUID
DATAFLAG_RESOURCE_GUID = 0x00000040
# This resources administrative fields
DATAFLAG_RESOURCE_ADMIN_FIELDS = 0x00000080
# This resource's drivers
DATAFLAG_RESOURCE_DRIVERS = 0x00000100
# This resource's jobs
DATAFLAG_RESOURCE_JOBS = 0x00000200
# This resource's notifications
DATAFLAG_RESOURCE_NOTIFICATIONS = 0x00000400
# This resouce's points of interest
DATAFLAG_RESOURCE_POIS = 0x00000800
# This resource's geofences
DATAFLAG_RESOURCE_GEOFENCES = 0x00001000
# This resource's report templates
DATAFLAG_RESOURCE_REPORT_TEMPLATES = 0x00002000
# This resource's units allowed for driver attachment
DATAFLAG_RESOURCE_DRIVER_ATTACHABLE_UNITS = 0x00004000
# This resource's driver groups
DATAFLAG_RESOURCE_DRIVER_GROUPS = 0x00008000
# This resource's trailers
DATAFLAG_RESOURCE_TRAILERS = 0x00010000
# This resource's trailer groups
DATAFLAG_RESOURCE_TRAILER_GROUPS = 0x00020000
# This resource's units allowed for trailer attachment
DATAFLAG_RESOURCE_TRAILER_ATTACHABLE_UNITS = 0x00040000
# This resource's orders
DATAFLAG_RESOURCE_ORDERS = 0x00080000
# This resource's geofence groups
DATAFLAG_RESOURCE_GEOFENCE_GROUPS = 0x00100000
# This resource's tags (passengers)
DATAFLAG_RESOURCE_TAGS = 0x00200000
# This resource's units allowed for tag attachment
DATAFLAG_RESOURCE_TAG_ATTACHABLE_UNITS = 0x00400000
# This resource's tag groups (passengers)
DATAFLAG_RESOURCE_TAG_GROUPS = 0x00800000
# All possible resource data flags
DATAFLAG_RESOURCE_ALL = 4611686018427387903

## Retranslator - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/retranslator
# This retranslator's basic properties
DATAFLAG_RETRANSLATOR_BASE = 0x00000001
# This retranslator's custom properties
DATAFLAG_RETRANSLATOR_CUSTOM_PROPERTIES = 0x00000002
# This retranslator's billing properties
DATAFLAG_RETRANSLATOR_BILLING_PROPERTIES = 0x00000004
# This retranslator's GUID
DATAFLAG_RETRANSLATOR_GUID = 0x00000040
# This retranslator's admin fields
DATAFLAG_RETRANSLATOR_ADMIN_FIELDS = 0x00000080
# This retranslator's state and configuration
DATAFLAG_RETRANSLATOR_CONFIGURATION = 0x00000100
# This retranslator's bound units
DATAFLAG_RETRANSLATOR_UNITS = 0x00000200
# All possible retranslator data flags
DATAFLAG_RETRANSLATOR_ALL = 4611686018427387903

## Route - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/route
# This route's basic properties
DATAFLAG_ROUTE_BASE = 0x00000001
# This route's custom properties
DATAFLAG_ROUTE_CUSTOM_PROPERTIES = 0x00000002
# This route's billing properties
DATAFLAG_ROUTE_BILLING_PROPERTIES = 0x00000004
# This route's GUID
DATAFLAG_ROUTE_GUID = 0x00000040
# This route's administrative fields
DATAFLAG_ROUTE_ADMIN_FIELDS = 0x00000080
# This route's configuration
DATAFLAG_ROUTE_CONFIGURATION = 0x00000100
# This route's checkpoints
DATAFLAG_ROUTE_CHECKPOINTS = 0x00000200
# This route's schedules
DATAFLAG_ROUTE_SCHEDULES = 0x00000400
# This route's rounds
DATAFLAG_ROUTE_ROUNDS = 0x00000800
# All possible route data flags
DATAFLAG_ROUTE_ALL = 4611686018427387903

## Unit - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/unit
# This unit's basic properties
DATAFLAG_UNIT_BASE = 0x00000001
# This unit's custom properties
DATAFLAG_UNIT_CUSTOM_PROPERTIES = 0x00000002
# This unit's billing properties
DATAFLAG_UNIT_BILLING_PROPERTIES = 0x00000004
# This unit's custom fields
DATAFLAG_UNIT_CUSTOM_FIELDS = 0x00000008
# This unit's image/icon
DATAFLAG_UNIT_IMAGE = 0x00000010
# This unit's messages
DATAFLAG_UNIT_MESSAGES = 0x00000020
# This unit's GUID
DATAFLAG_UNIT_GUID = 0x00000040
# This unit's administrative fields
DATAFLAG_UNIT_ADMIN_FIELDS = 0x00000080
# This unit's advanced properties
DATAFLAG_UNIT_ADVANCED_PROPERTIES = 0x00000100
# This unit's available for current moment commands
DATAFLAG_UNIT_CURRENT_MOMENT_COMMANDS = 0x00000200
# This unit's last message and position
DATAFLAG_UNIT_LAST_MESSAGE = 0x00000400
# This unit's sensors
DATAFLAG_UNIT_SENSORS = 0x00001000
# This unit's counters
DATAFLAG_UNIT_COUNTERS = 0x00002000
# This unit's maintenance
DATAFLAG_UNIT_MAINTENANCE = 0x00008000
# This unit's report configuration, trip detector, and fuel consumption
DATAFLAG_UNIT_REPORT_CONFIGURATION = 0x00020000
# This unit's available commands
DATAFLAG_UNIT_AVAILABLE_COMMANDS = 0x00080000
# This unit's message parameters
DATAFLAG_UNIT_MESSAGE_PARAMETERS = 0x00100000
# This unit's connection status
DATAFLAG_UNIT_CONNECTION_STATUS = 0x00200000
# This unit's position
DATAFLAG_UNIT_POSITION = 0x00400000
# This unit's profile files
DATAFLAG_UNIT_PROFILE_FIELDS = 0x00800000
# All possible unit data flags
DATAFLAG_UNIT_ALL = 4611686018427387903

## Unit Groups - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/group
# This group's basic properties
DATAFLAG_GROUP_BASE = 0x00000001
# This group's custom properties
DATAFLAG_GROUP_CUSTOM_PROPERTIES = 0x00000002
# This group's billing properties
DATAFLAG_GROUP_BILLING_PROPERTIES = 0x00000004
# This group's custom fields
DATAFLAG_GROUP_CUSTOM_FIELDS = 0x00000008
# This group's image/icon
DATAFLAG_GROUP_IMAGE = 0x00000010
# This group's GUID
DATAFLAG_GROUP_GUID = 0x00000040
# This group's administrative fields
DATAFLAG_GROUP_ADMIN_FIELDS = 0x00000080
# All possible group data flags
DATAFLAG_GROUP_ALL = 4611686018427387903

## User - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/user
# This user's basic properties
DATAFLAG_USER_BASE = 0x00000001
# This user's custom properties
DATAFLAG_USER_CUSTOM_PROPERTIES = 0x00000002
# This user's billing properties
DATAFLAG_USER_BILLING_PROPERTIES = 0x00000004
# This user's custom fields
DATAFLAG_USER_CUSTOM_FIELDS = 0x00000008
# This user's messages
DATAFLAG_USER_MESSAGES = 0x00000020
# This user's GUID
DATAFLAG_USER_GUID = 0x00000040
# This user's administrative fields
DATAFLAG_USER_ADMIN_FIELDS = 0x00000080
# This user's other properties
DATAFLAG_USER_OTHER_PROPERTIES = 0x00000100
# This user's notifications
DATAFLAG_USER_NOTIFICATIONS = 0x00000200
# All possible user data flags
DATAFLAG_USER_ALL = 4611686018427387903

### Settings flags
## User - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/user/update_user_flags
# This user is disabled
SETTINGSFLAG_USER_DISABLED = 0x01
# This user cannot change their password
SETTINGSFLAG_USER_CANNOT_CHANGE_PASSWORD = 0x02
# This user can create objects
SETTINGSFLAG_USER_CAN_CREATE_ITEMS = 0x04
# This user cannot change settings
SETTINGSFLAG_USER_CANNOT_CHANGE_SETTINGS = 0x10
# This user can send SMS messages
SETTINGSFLAG_USER_CAN_SEND_SMS = 0x20

### Token flags
## General - https://sdk.wialon.com/wiki/en/sidebar/remoteapi/apiref/format/token
# Online tracking
TOKENFLAG_ONLINE_TRACKING = 0x100
# View access to most data
TOKENFLAG_VIEW_ACCESS = 0x200
# Modification of non-sensitive data
TOKENFLAG_MANAGE_NONSENSITIVE = 0x400
# Modification of sensitive data
TOKENFLAG_MANAGE_SENSITIVE = 0x800
# Modification of critical data, including message deletion
TOKENFLAG_MANAGE_CRITICAL = 0x1000
# Modification of communication data
TOKENFLAG_COMMUNICATION = 0x2000
# Unlimited operation as authorized user
TOKENFLAG_MANAGE_ALL = -1
