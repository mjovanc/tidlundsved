# This is be removed at a later point as we intend to keep product types in DB rather then hardcoded here

PRODUCT_TYPE = (
    ('Blandat lövträd', 'Blandat lövträd'),
    ('Björkved', 'Björkved'),
    ('Bokved', 'Bokved'),
    ('Askved', 'Askved'),
    ('Övrigt', 'Övrigt'),
)

BLANDAT_LOVTRAD_CHOICES = (
    ('Löst nykluven (kubik)', 'Löst nykluven (kubik)'),
    ('Löst torr (kubik)', 'Löst torr (kubik)'),
    ('Nykluven (kubik på pall)', 'Nykluven (kubik på pall)'),
    ('Torr (kubik)', 'Torr (kubik)'),
)

BJORKVED_CHOICES =(
    ('Löst nykluven (kubik)', 'Löst nykluven (kubik)'),
    ('Löst torr (kubik)', 'Torr löst (kubik)'),
    ('Torr (kubik på pall)', 'Torr (kubik på pall)'),
    ('Nykluven på pall (st)', 'Nykluven på pall (st)'),
    ('40 liters säck (st)', '40 liters säck (st)'),
)

BOKVED_CHOICES = (
    ('Löst nykluven (kubik)', 'Löst nykluven (kubik)'),
    ('Löst torr (kubik)', 'Löst torr (kubik)'),
    ('Torr (kubik på pall)', 'Torr (kubik på pall)'),
    ('Nykluven på pall (st)', 'Nykluven på pall (st)'),
    ('40 liters småsäck (st)', '40 liters småsäck (st)'),
)

ASKVED_CHOICES = (
    ('Löst nykluven (kubik)', 'Löst nykluven (kubik)'),
    ('Löst torr (kubik)', 'Löst torr (kubik)'),
    ('Torr på pall (st)', 'Torr på pall (st)'),
    ('40 liters småsäck (st)', '40 liters småsäck (st)'),
)

OTHER_CHOICES = (
    ('Pellets', 'Pellets'),
    ('Briketter', 'Briketter'),
    ('Huggkubbe', 'Huggkubbe'),
    ('Spån (kubik)', 'Spån (kubik)'),
)

DELIVERY_OPTIONS = (
    ('Hämta på plats', 'Hämta på plats'),
    ('Utkörning', 'Utkörning')
)
