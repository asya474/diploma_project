yasha = User(first_name='yasha', last_name='kramarenko', email='yashaka@gmail.com', ...)
registration_page.open()
registration_page.register(yasha)
registration_page.should_have_registered(yasha)