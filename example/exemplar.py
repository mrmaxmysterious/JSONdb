import JSONdb as JDB

# Input a "schema" in here, if you need to create one dont put anything
yes = JDB.db("servers")

# These are all the current available options

#print(yes.findById("ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"))
#print(yes.createId())
#print(yes.insert("03747783",{'serverName': "hetzner1", 'status': True}))
#print(yes.findBy('balance', 350))
#print(yes.findAll())
#print(yes.countDocuments())
#print(yes.createSchema("servers", {'serverName': {'required': True, 'type': 'string'}, 'status': {'required': True, 'type': 'bool'}}))
