import requests
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import User, db, Merch
from app.shop.forms import SellMerchForm

shop = Blueprint('shop', __name__, template_folder='shoptemplates')

@shop.route('/shop', methods=["GET", "POST"])
def goToShop():
    merch = Merch.query.all()
    return render_template('shop.html', merch=merch)

@shop.route('/shop/<int:merch_id>', methods=["GET", "POST"])
def viewMerch(merch_id):
    merch = Merch.query.get(merch_id)
    return render_template('singleMerch.html', merch=merch)

@shop.route('/cart')
def goToCart():
    cart = current_user.cart.all()
    return render_template('cart.html', cart=cart)








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

