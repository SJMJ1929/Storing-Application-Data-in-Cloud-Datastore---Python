"""
Create and persist and entity for each question
The Datastore key is the equivalent of a primary key in a relational database.
There are two main ways of writing a key:
1. Specify the kind, and let Datastore generate a unique numeric id
2. Specify the kind and a unique string id
"""
def save_question(question):
# TODO: Create a key for a Datastore entity
# whose kind is Question

    key = datastore_client.key('Question')

# END TODO

# TODO: Create a Datastore entity object using the key

    q_entity = datastore.Entity(key=key)

# END TODO

# TODO: Iterate over the form values supplied to the function

    for q_prop, q_val in question.iteritems():

# END TODO

# TODO: Assign each key and value to the Datastore entity

        q_entity[q_prop] = q_val

# END TODO

# TODO: Save the entity

    datastore_client.put(q_entity)

# END TODO