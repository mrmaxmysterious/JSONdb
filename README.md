# JSONdb

So, I'm sure you once needed a module so desperately to create a database, but with JSON files??!!!!! Well, that's what I made. I was BORED, OKAY??

Check the example file if you don't know what to do.

**DO NOT PUT THIS IN ANY DIRECTORIES APART FROM THE MAIN ONE!!!!!! This needs to be in your main folder, not in src/JSONdb.** Ya get what I mean blud?!!!?!!?1111
But also, make sure this is in a folder called `JSONdb` otherwise nothing will work.

 # Exemplars:

```py
import JSONdb

db = JSONdb.db("schema name")
# If you are creating a new schema, DO NOT PUT ANY SCHEMA NAME IN THERE!

db.createId()
# Creates a unique ID.

db.findAll()
# Fetches all documents in the JSON db.

db.findBy(name, value)
# Fetches all documents with 'name' as the 'value' you put in.

db.findById(id)
# More specific. If you know the very long Id of the document, use that here to find the document.

db.countDocuments()
# Counts all documents in the JSON db.

db.insert(documentName, dictionary)
# This is how you put things in the JSON db. You put in a document name, and then you can put in what you want to input as a DICTIONARY to the db. IT MUST USE THE CORRECT TEMPLATE AS PER THE SCHEMA BASEPLATE!

db.createSchema(schemaName, baseplate)
# This is how you create new schemas (JSON files). You put in a document name so you can actually use the db, and then the baseplate HAS TO USE THE FOLLOWING SORT OF TEMPLATE:
# {'name': {'required': True/False, 'type': "int/string/float/bool/list/dict/any"}, ...}
# Change the name to whatever you want that input to be stored as, this baseplate will be followed throughout the whole entire database schema.
```

I'll add more things when i feel like it lol
