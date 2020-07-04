"# Django_UseractivityAPI" 
<div>
<p>Useractivity is an API for the platform where Admin can keep a track of the daily basis user activity.
</p>
<p>API is built uisng (Django, Django REST framework, serializers, ORM and sqlite3)</p>
</div>  
<h2>Screenshots and Link</h2>
    <h3>Screenshots = https://github.com/melwinmpk/Django_UseractivityAPI/tree/master/Screenshots</h3>
    <h3>Link = https://useractivity-restapi.herokuapp.com/</h3>
<h2>Buisness Logic</h2>
    <h3>Admin Work Flow</h3>
    <ul>
        <li>Admin can create new User</li>
        <li>Add the activity period to the respective User</li>
        <li>Admin can list all the Users along with the activity perion</li>
        <li>Admin can even list all the  activity period of the selected Users </li>
        <li>Admin can Modify the Users Data</li>
        <li>Admin can Modify the activity period of the selected Users</li>
        <li>Admin can Delete the Users Data</li>
        <li>Admin can Delete the Selective activity period</li>       
    </ul>
<h2>Dummy Creation</h2>
	<ul>
		<li>Just run the link 10 Users will be popluated it to the DataBase along with the Activity Period</li>
        <li>https://useractivity-restapi.herokuapp.com/api/users/populateuser/</li>       
    </ul>
	
<h2>API ENDPOINTS</h2>
        <div class="endpoints_div">
            <h3>User</h3>
            <ul>
                <li>EndPoint: <span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/userlistserializers</span></li>
                <li><span>Data that needed to be passed </span>
                    <pre>
                        {
                            "real_name": "Tom",
                            "tz": "America/Los_Angeles"
                        }
                    </pre>    
                </li>
            </ul>
            <h3>User Create and Listing  (Creation Post method and listing Get Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/userlistserializers</span></li>
                <li><span>Data that needed to be passed for Task Creation </span>
                    <pre>
                        {
                            "real_name": "Tom",
                            "tz": "America/Los_Angeles"
                        }
                    </pre>
                </li>
            </ul>    
            <h3>User Delete and Update (Deletion Delete method and Update Put Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/userserializers</span></li>
                <li><span>Data that needed to be passed for User Update for User Delete only id is enough</span>
                    <pre>
			{
				"id":"99",
				"real_name": "Tom",
				"tz": "America/Los_Angeles"
			}
                    </pre>
                </li>
            </ul>
        </div>
        <div class="endpoints_div">
            <h3>Activity Period</h3>
            <ul>
                <li>EndPoint: <span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/usractivitylistserializers/</span></li>
                <li><span>Data that needed to be passed </span>
                    <pre>
                        {
				"userid": "90",
				"start_time": "Feb 3 2020  1:33PM",
				"end_time": "Feb 3 2020 1:54PM"
			}
                    </pre>    
                </li>
            </ul>
            <h3>Activity Period Create and Listing of the User (Creation Post method and listing Get Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/usractivitylistserializers</span></li>
                <li><span>Data that needed to be passed for User Activity Creation </span>
                    <pre>
						{
							"userid": "90",
							"start_time": "Feb 3 2020  1:33PM",
							"end_time": "Feb 3 2020 1:54PM"
						}
                    </pre>
                </li>
            </ul>    
            <h3>Activity Period Delete and Update (Deletion Delete method and Update Put Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://useractivity-restapi.herokuapp.com/</span><span>api/users/usractivityserializers</span></li>
                <li><span>Data that needed to be passed for User Update for User Delete only id is enough</span>
                    <pre>
                        {
							"id":"99",
							"real_name": "Tom",
							"tz": "America/Los_Angeles"
						}
                    </pre>
                </li>
            </ul>
        </div>
