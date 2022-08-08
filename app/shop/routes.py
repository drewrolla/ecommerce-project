import requests
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import User, db, Merch

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

@shop.route('/shop', methods=["GET", "POST"])
def goToShop():
    merch = Merch.query.all()
    return render_template('shop.html', merch=merch)

@shop.route('/cart', methods=["GET", "POST"])
def goToCart():
    user = User.query.get(current_user.id)
    cart = user.cart.all()
    return render_template('cart.html', cart=cart)

@shop.route('/add/<string:name>')
@login_required
def addToCart(name):
    merch = Merch.query.filter_by(name=name).first()
    current_user.cart.append(merch)
    db.session.commit()
    flash('Item added to cart.', 'success')
    return redirect(url_for('shop.goToCart'))

@shop.route('/remove/<string:name>')
@login_required
def removeFromCart(name):
    merch = Merch.query.filter_by(name=name).first()
    current_user.cart.remove(merch)
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('shop.goToCart'))

@shop.route('/remove')
@login_required
def emptyCart():
    merch = Merch.query.all()
    for m in merch:
        if m in current_user.cart:
            current_user.cart.remove(m)
            db.session.commit()
    flash('You have no items in your cart.', 'success')
    return redirect(url_for('shop.goToCart'))

# look at one product in particular
@shop.route('/shop/<int:merch_id>')
def viewItem(merch_id):
    merch = Merch.query.get(merch_id)
    return render_template('single.html', merch=merch)





# keep getting error with it saying that there is an attributeerror with my submit button, 
# something along the lines of "no creation counter"
# create products
# @shop.route('/shop/sell', methods=["GET", "POST"])
# @login_required
# def sellMerch():
#     form = SellMerchForm()
#     if request.method=="POST":
#         if form.validate():
#             name = form.name.data
#             price = form.price.data
#             description = form.description.data
#             img_url = form.img_url.data

#             merch = Merch(name, price, description, img_url)
#             merch.saveMerch()
#             flash('Your item will be listed shortly!', 'success')
#         else:
#             flash('Error, please try again.', 'danger')
#     return render_template('sellMerch.html', form=form)

