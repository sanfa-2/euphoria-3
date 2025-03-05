# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Slide, CategoryForMen, CategorForWomen, Brand, Limelight, Testimonial, Product, Category, Product, OrderItem, Order




def index(request):
    slides = Slide.objects.all()
    mens = CategoryForMen.objects.prefetch_related('category').all() 
    womens = CategorForWomen.objects.prefetch_related('category').all()
    brands = Brand.objects.all()
    limelights = Limelight.objects.select_related().all() 
    testimonials = Testimonial.objects.all()
    categories = Category.objects.prefetch_related('products').all() 
    categories = Category.objects.prefetch_related('products').all() 
    all_products = Product.objects.all()

    cart = request.session.get('cart', {})
    cart_items = []
    if cart:
        total_price = 0
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            total_price += product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity,
            })
    else:
        cart_items = []
   
    context = {
        'slides': slides,
        'mens': mens,
        'womens': womens,
        'brands': brands,
        'limelights': limelights,
        'testimonials': testimonials,
        'categories': categories,
        'all_products': all_products, 
        'cart_items': cart_items,  
        
        
    }

    return render(request, 'index.html', context=context)



def category_products(request, category_id):
    category_type = request.GET.get('type')

    second_related_category = None  
    products = []

    if category_type == 'men':
        category = get_object_or_404(CategoryForMen, id=category_id)
        
        related_categories = category.category.all()
       
        second_related_category = related_categories[1] if len(related_categories) > 1 else None


        if second_related_category:
            print(f"Second related category for Men: {second_related_category.name}")
        products = Product.objects.filter(category=second_related_category).distinct() if second_related_category else []
    
    elif category_type == 'women':
        category = get_object_or_404(CategorForWomen, id=category_id)

        related_categories = category.category.all()
        second_related_category = related_categories[1] if len(related_categories) > 1 else None

        if second_related_category:
            print(f"Second related category for Women: {second_related_category.name}")

        products = Product.objects.filter(category=second_related_category).distinct() if second_related_category else []
    
    else:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category).distinct()

    context = {
        'category': category,
        'products': products,
        'category_type': category_type,
        'second_related_category': second_related_category,
    }
    return render(request, 'category_products.html', context)



def men_categories(request):
    men_category = Category.objects.filter(name__iexact="Men").first()  
    products = Product.objects.filter(category=men_category) if men_category else Product.objects.none()

    context = {
        'category': men_category,
        'products': products,
        'first_related_category': men_category,  
    }
    return render(request, 'category_products.html', context)



def women_categories(request):
    women_category = Category.objects.filter(name__iexact="Women").first() 
    products = Product.objects.filter(category=women_category) if women_category else Product.objects.none()

    context = {
        'category': women_category,
        'products': products,
        'first_related_category': women_category, 
    }
    return render(request, 'category_products.html', context)




def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    first_category = product.category.first()
    categories = product.category.all() 

    if len(categories) > 1:
        second_category = categories[1]  
        similar_products = Product.objects.filter(
            category=second_category
        ).exclude(id=product.id).distinct() 
    else:
        similar_products = []  

    return render(request, 'detail.html', {
        'product': product,
        'first_category': first_category,
        'similar_products': similar_products,
    })




def search(request):
    query = request.GET.get('q', '').strip() 
    products = Product.objects.filter(
        Q(title__icontains=query) | Q(category__name__icontains=query)
    ).distinct() if query else Product.objects.none() 
    
    return render(request, 'search_products',{
        'products': products, 
        'query': query,     
    })


def cart_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to view cart.")
        return redirect('/users/login')
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to add to cart.")
        return redirect('/users/login')
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('web:cart_view')

def remove_from_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to remove cart.")
        return redirect('/users/login')
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('web:cart_view')


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to checkout.")
        return redirect('/users/login')

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect('web:cart_view')
    
    
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': float(product.price * quantity),  
        })

    order = Order.objects.create(user=request.user, is_paid=False) 

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
        )
    
    request.session['cart'] = {}
    
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'order': order, 
    }

    return render(request, 'purchased_products.html', context)



def wish_cart_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to view wish items.")
        return redirect('/users/login')  
    
   
    wish_cart = request.session.get('wish_cart', {}) 
    wish_cart_items = [] 
    total_price = 0 

   
    for product_id, quantity in wish_cart.items():
        product = get_object_or_404(Product, id=product_id)  
        total_price += product.price * quantity 
        wish_cart_items.append({
            'product': product,  
            'quantity': quantity,
            'total_price': product.price * quantity, 
        })

    return render(request, 'wish_cart.html', {
        'wish_cart_items': wish_cart_items, 
        'total_price': total_price, 
    })


def add_to_wish_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to add wish items.")
        return redirect('/users/login') 

    wish_cart = request.session.get('wish_cart', {}) 

    wish_cart[str(product_id)] = wish_cart.get(str(product_id), 0) + 1
    request.session['wish_cart'] = wish_cart 
    messages.success(request, "Product added to your wish cart!") 

    return redirect('web:wish_cart_view') 


def remove_from_wish_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to proceed to remove wish items.")
        return redirect('/users/login')  
    
    wish_cart = request.session.get('wish_cart', {}) 

    if str(product_id) in wish_cart:
        del wish_cart[str(product_id)]  
        request.session['wish_cart'] = wish_cart  
        messages.success(request, "Product removed from your wish cart!")  
    else:
        messages.info(request, "Product not found in your wish cart.") 
    
    return redirect('web:wish_cart_view')   



