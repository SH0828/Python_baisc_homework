cart = {
    '사과': {'quantity': 2, 'price_per_item': 1000},
    '바나나': {'quantity': 3, 'price_per_item': 800},
    '오렌지': {'quantity': 1, 'price_per_item': 1500}
}

total_price = 0

print("쇼핑 카트:")
for item, info in cart.items():
    item_total = info['quantity'] * info['price_per_item']
    print(f"{item}: {info['quantity']}개 (개당 {info['price_per_item']}원) = {item_total}원")
    total_price += item_total

print(f"총 가격: {total_price}원")