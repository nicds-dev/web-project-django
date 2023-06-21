def import_total_price(request, total = 0):
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total += (float(value["price"]))
    else:
        total = 0
    return {"import_total_price": total}
