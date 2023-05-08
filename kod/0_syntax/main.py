is_delivered = True
is_notified = False

# good
if is_delivered and is_notified:
    is_done = True
else:
    is_done = False

# but that's better
is_done = is_delivered and is_notified

# good counting
default_order = ['coolaid']
orders = []
if len(orders) == 0:
    print('There are no orders')

# better counting
if not orders:  # use object's boolean value
    print('There are no orders')

# what about this?
final_order = orders or default_order
print(final_order)
