import unittest
import os 
import json
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #extend sys path to discover app package 
from app import create_app,db

class BucketlistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case """

    def setUp(self):
        self.app=create_app(config_name="testing")
        self.client= self.app.test_client
        self.bucketlist={'name':'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """teardown all initailized variables"""
        with self.app.app_context():
            #drop all tables 
            db.session.remove()
            db.drop_all()

    def test_bucketlist_creation(self):
        """Test API can create a bucketlist (POST request)"""
        res=self.client().post('/bucketlists',data=self.bucketlist)
        self.assertEqual(res.status_code,201)
        self.assertIn('Go to Borabora',str(res.data))

    def test_api_can_get_all_buckerlists(self):
        """Test API can get a bucketlist (GET request)."""
        self.test_bucketlist_creation() # recall the test_bucketlist_creation method above 
        res = self.client().get('/bucketlists')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_bucketlist_by_id(self):
        """Test API can get a single bucketlist by using it's id."""
        self.test_bucketlist_creation() # recall the test_bucketlist_creation method above 
        result = self.client().get(
            '/bucketlists/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Go to Borabora', str(result.data))

    def test_bucketlist_can_be_edited(self):
        self.test_bucketlist_creation() # recall the test_bucketlist_creation method above 
        """Test API can edit an existing bucketlist.(PUT request)"""
        rv = self.client().put('/bucketlists/1',data={
            "name":"Dont just eat but also pray and love :-)"
        })
        self.assertEqual(rv.status_code,200)
        results = self.client().get('/bucketlists/1')
        self.assertIn('Dont just eat',str(results.data))

    def test_bucketlist_deletion(self):
        """Test API can delete an exisiting  buckectlist.( DELETE request)."""
        self.test_bucketlist_creation() # recall the test_bucketlist_creation method above 
        res = self.client().delete('/bucketlists/1')
        self.assertEqual(res.status_code,200)
        #Test to see if it exists , should return a 404
        result = self .client().get('/bucketlists/1')
        self.assertEqual(result.status_code,404)


if __name__=="__main__":
    unittest.main()

            




    

