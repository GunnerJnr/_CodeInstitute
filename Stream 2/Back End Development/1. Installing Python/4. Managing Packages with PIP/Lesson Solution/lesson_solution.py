import simplejson
 
raw_json = """
[
   "foo",
   {
       "bar": ["baz", null, 1.0, 2]
   }
]
"""
 
decoded_json = simplejson.loads(raw_json)
print decoded_json
print decoded_json[0]
