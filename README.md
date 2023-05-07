# little-lemon-API
project littlelemon API for API course from Meta


<hr>
<br>

# ENDPOINTS

- ### user autherization
i use the built-in endpoints in djoser , for more see [djoser docs](https://djoser.readthedocs.io/en/latest/)


<br> <br> <br>


- ### Menu

##### Endpoint : http://127.0.0.1:8000/api/menu-items/

##### Methods : GET , POST , PUT , DELETE...

for Managers , they can make POST , PUT , DELETE call requset , but customers can't

to GET a specific Menu Item , you can add its id at the end of the endpoint : api/menu-items/2

<br> <br> <br>

- ### Catigories

##### Endpoint : http://127.0.0.1:8000/api/catigories/

##### Methods : GET , POST , PUT , DELETE...

for Managers , they can make POST , PUT , DELETE call requset , but customers can't

to GET a specific catigory , you can add its id at the end of the endpoint : api/catigories/2

<br> <br> <br>

- ### Carts

##### Endpoint : http://127.0.0.1:8000/api/carts/

##### Methods : GET , POST , PUT , DELETE...

for Managers , they can make POST , PUT , DELETE call requset , but customers can't

Customers can make GET request to see thier own cart. in the other hand, Managers can see all the users' carts

to GET a specific cart , you can add its id at the end of the endpoint : api/carts/2

<br> <br> <br>

- ### Orders

##### Endpoint : http://127.0.0.1:8000/api/orders/

##### Methods : GET , POST , PUT , DELETE...

for Managers , they can make POST , PUT , DELETE call requset , but customers can't

Customers can make GET request to see thier own order. in the other hand, Managers can see all the users' orders

to GET a specific order , you can add its id at the end of the endpoint : api/orders/2

<br> <br> <br>

- ### Order Items

##### Endpoint : http://127.0.0.1:8000/api/order_items/

##### Methods : GET , POST , PUT , DELETE...

for Managers , they can make POST , PUT , DELETE call requset , but customers can't

Customers can make GET request to see thier own order items. in the other hand, Managers can see all the users' orders items

to GET a specific order , you can add its id at the end of the endpoint : api/order_items/2


<br> <br> <br>


- ### add to cart ( users )

##### Endpoint : http://127.0.0.1:8000/api/cart/add-item/

##### Methods : POST

##### parameters : [itemId , quantity]

adds a specific item to the user's cart

<br> <br> <br>


- ### Place Order ( users )

##### Endpoint : http://127.0.0.1:8000/api/place_order/

##### Methods : POST

##### parameters : []

place order with the items in the user's cart , if no items found it returns ERROR 403.


<br> <br> <br>


- ### Assign user to group ( managers )

##### Endpoint : http://127.0.0.1:8000/api/groups/<slug:groupName>/users/

##### Methods : POST

##### parameters : [userId]

assign the user with id = userId to a group

**Note : you should pass the group name to be replaced with <slug:groupName>**

<br> <br> <br>


- ### remove user from group ( managers )

##### Endpoint : http://127.0.0.1:8000/api/groups/<slug:groupName>/users/<int:pk>/

##### Methods : DELETE

##### parameters : []

reomve the user with id = pk from the group with name = groupName



<br> <br> <br>


- ### assign delivery crews to orders ( managers )

##### Endpoint : http://127.0.0.1:8000/api/assign_crew/

##### Methods : POST

##### parameters : [userId , orderId]


<br> <br> <br>


- ### assign delivery crews to orders ( crew / managers )

##### Endpoint : http://127.0.0.1:8000/api/mark_as_delivered/

##### Methods : POST

##### parameters : [orderId]
