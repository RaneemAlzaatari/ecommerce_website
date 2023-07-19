Ecommerce_website:
    About_this_App:
    An e-commerce application where users can purchase products and let 
    them visit our website, and they can view any product details for free. 
    The store owner can add his products and display them on the home 
    page, upload pictures, add prices, and the ability to edit and delete 
    them if he wants. The user needs to create an account on our website 
    to add a product to the cart.
    
App_Overview:
     Create products:
    Endpoint: (post) CreateProduct
     The store owner creates his products in the database.
     
     Products_List_Page:
    Endpoint:(Get) AllProducts
    This page displays all the available products on the website.
    
     Product_Details_Page:
    Endpoint:(Get) DetailsProduct
    This page displays the details of the Product which user has selected from 
    the products list page. Here, the user can see all the info of the Product 
    such as product name, description, in stock or out of stock . For Admins, the 
    website provides two more functionalities such as Updating the product 
    and secondly deleting the product.
    
     Product_Edit_Page:
    Endpoint:(put) UpdateProduct
    Only admins can visit this page, the page handles the editing of the Product in 
    terms of image, name , description, price and in stock status.
    
     Product_delete_page:
    Endpoint:(delete) DeleteProduct
    Only admins can visit this page, and the page handles deletion of the product 
    along with its details.
    
     Add_images_product:
    Endpoint:(post) AddImageProduct
    Add more than one image of the same product
    
     Image_by_id_product:
    Endpoint: (Get) ImageProductById
     View all product images
     
     Create cart:
    Endpoint: (post) CreateCart
    Create a shopping cart for the user
    
     Add_product_to_cart:
    Endpoint:(post) AddProductToCart
    The user can add products to the market cart to purchase them 
    later
    
     Cart_Item_By_Id:
    Endpoint:(Get) CartItemById
     The user can view his products in the cart and the ability to 
    modify the quantity he ordered
     
     Checkout :
    Endpoint: (delete) CheckoutProduct
     The user can remove the product from the cart
     
     Checkout _part:
    Endpoint: (post) PartCheckoutProduct
    The user can reduce the quantity of the product that he added to 
    the cart
    
     Search Product:
    Endpoint :(Get) SearchProduct
    Search for products
    
Tools:
   Python 3
   postgresql
   django rest framework apis
   TokenAuthentication From Drf
  
Installation:
  after downloading/cloning the repository code follow below steps:
   Backend
   (for both linux and windows)
  1. Move in backend folder through terminal and run following 
  commands,
  python3 -m venv env (for windows --> python -m venv 
  env)
  source env/bin/activate (for windows --
  > env\scripts\activate)
  pip install -r requirements.txt (same for both)
  python manage.py runserver (same for both)

Futures:
   Payment
   Filters
   Scan Qr code to product
   Orders
   Notifications
   Multi language
 
