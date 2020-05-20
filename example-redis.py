from rgsync import RGWriteBehind, RGWriteThrough
from rgsync.Connectors import RedisConnector, RedisConnection

'''
Create Redis connection object
'''
print("before RedisConnection")
connection = RedisConnection('default', 'default', 'redis-14555.jph-vu-chi.demo.redislabs.com', '14555')
print("after RedisConnection")

'''
Create Redis member redis json
members - Redis hash to put the data
member_id - primary key
'''
membersConnector = RedisConnector(connection, 'members', 'member_id')

membersMappings = {
	'id':'id',
	'firstName':'firstName',
	'lastName':'lastName',
	'dependentSequence':'dependentSequence'
}

RGWriteBehind(GB,  keysPrefix='member', mappings=membersMappings, connector=membersConnector, name='PersonsWriteBehind',  version='99.99.99')

RGWriteThrough(GB, keysPrefix='__',     mappings=membersMappings, connector=membersConnector, name='PersonsWriteThrough', version='99.99.99')

