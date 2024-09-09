from flet import *

def main(page:Page):
    page.title = "Unit Converter"
    page.window.width = 390
    page.window.height = 750
    page.scroll = "auto"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = "#FFFFFF"

    page.update()

    

    def change_route(route):
        page.views.clear()
        
        if page.route == "/unit_converter":
            page.views.append(unit_converter_page())
        elif page.route == "/about":
            page.views.append(about())
        elif page.route == "/":
            page.views.append(Home_page())

        page.update()
    def convert_units(e):
        value = float(input_value.value)
        if from_unit.value == "Meter" and to_unit.value == "Kilometer":
            result.value = str(value / 1000)
        elif from_unit.value == "Kilometer" and to_unit.value == "Meter":
            result.value == str(value * 1000)
        elif from_unit.value == "Meter" and to_unit.value == "Mile":
            result.value = str(value * 0.000621371)
        elif from_unit.value == "Mile" and to_unit.value == "Meter":
            result.value = str(value / 0.000621371)
        elif from_unit.value == "Meter" and to_unit.value == "Yard":
            result.value = str(value * 1.09361)
        elif from_unit.value == "Yard" and to_unit.value == "Meter":
            result.value = str(value / 1.09361)
        ################## ---- weit ------ ####################
        elif from_unit.value == "Kilogram" and to_unit.value == "Gram":
            result.value = str(value * 1000)
        elif from_unit.value == "Gram" and to_unit.value == "Kilogram":
            result.value = str(value / 1000)
        elif from_unit.value == "Pound" and to_unit.value == "Kilogram":
            result.value = str(value * 0.453592)
        elif from_unit.value == "Kilogram" and to_unit.value == "Pound":
            result.value = str(value / 0.453592)
        ################### ---- size ------ ####################
        elif from_unit.value == "Liter" and to_unit.value == "Milliliter":
            result.value = str(value * 1000)
        elif from_unit.value == "Milliliter" and to_unit.value == "Liter":
            result.value = str(value / 1000)
        ################### ---- size ------ ####################
        elif from_unit.value == "Hour" and to_unit.value == "Minute":
            result.value = str(value * 60)
        elif from_unit.value == "Minute" and to_unit.value == "Hour":
            result.value = str(value / 60)
        ################### ---- size ------ ####################
        elif from_unit.value == "Celsius" and to_unit.value == "Fahrenheit":
            result.value = str((value * 9/5) + 32)
        elif from_unit.value == "Fahrenheit" and to_unit.value == "Celsius":
            result.value = str((value - 32) * 5/9)
        elif from_unit.value == "Celsius" and to_unit.value == "Kelvin":
            result.value = str(value + 273.15)
        elif from_unit.value == "Kelvin" and to_unit.value == "Celsius":
            result.value = str(value - 273.15)

                
        page.update()

    input_value = TextField(label="Enter Value",
                            width=200,
                            color="#BDC3C7",
                            border_color="#3498DB")
    from_unit = Dropdown(label="From Unit",
                         border_color="#3498DB",
                         color="#BDC3C7",
                         width=150,
                         options=[  dropdown.Option("Meter"),dropdown.Option("Kilometer"),
                                    dropdown.Option("Mile"), dropdown.Option("Yard"),
                                    dropdown.Option("Foot"), dropdown.Option("Inch"),
                                    dropdown.Option("Kilogram"), dropdown.Option("Gram"),
                                    dropdown.Option("Pound"), dropdown.Option("Ounce"),
                                    dropdown.Option("Liter"), dropdown.Option("Milliliter"),
                                    dropdown.Option("Gallon"), dropdown.Option("Second"),
                                    dropdown.Option("Minute"), dropdown.Option("Hour"),
                                    dropdown.Option("Day"), dropdown.Option("Celsius"),
                                    dropdown.Option("Fahrenheit"),dropdown.Option("Kelvin")])
    to_unit = Dropdown(label="To Unit",
                       color="#BDC3C7",
                       border_color="#3498DB",
                       width=150,
                       options=[    dropdown.Option("Meter"),dropdown.Option("Kilometer"),
                                    dropdown.Option("Mile"),dropdown.Option("Yard"),
                                    dropdown.Option("Foot"),dropdown.Option("Inch"),
                                    dropdown.Option("Kilogram"),dropdown.Option("Gram"),
                                    dropdown.Option("Pound"),dropdown.Option("Ounce"),
                                    dropdown.Option("Liter"),dropdown.Option("Milliliter"),
                                    dropdown.Option("Gallon"),dropdown.Option("Second"),
                                    dropdown.Option("Minute"),dropdown.Option("Hour"),
                                    dropdown.Option("Day"),dropdown.Option("Celsius"),
                                    dropdown.Option("Fahrenheit"),dropdown.Option("Kelvin")])
    result = TextField(label="Result",
                       width=200,
                       border_color="#F1C40F",
                       read_only=True)
    convert_button = ElevatedButton(text="CONVERT",
                                    color="#FFFFFF",
                                    bgcolor="#1ABC9C",
                                    on_click=convert_units,
                                    width=150,
                                    height=50)

    def Home_page():
        def navigate(option):
            if option == "about":
                page.go("/about")
            elif option == "contact":
                page.go("/contact")
            elif option == "Github":
                page.launch_url("https://github.com/ismaillmouden")

        return View(
            "/",
            controls=[
                Row(controls=[
                    PopupMenuButton(items=[
                        PopupMenuItem(text="About",
                                      on_click=lambda _:navigate("about")),
                        PopupMenuItem(text="GitHub",
                                      on_click=lambda _:navigate("Github"))
                    ])
                ],alignment=alignment.center),

                Row(controls=[
                    Text("\n\n\n\n")
            ]),
                Row(controls=[
                Image(src="unit_converter.png",width=200,height=200)
            ],alignment=MainAxisAlignment.CENTER),
            Row(controls=[
                Text("Unit Converter App",color="#FFFFFF",size=25),],alignment=MainAxisAlignment.CENTER)
             ,Row(controls=[
                 ElevatedButton("Enter",
                                color="#DBC3C7",
                                bgcolor="#1ABC9C",
                                width=100,
                                height=50,
                                on_click=lambda _e: page.go("/unit_converter"))
             ],alignment=MainAxisAlignment.CENTER),]
            )
    

    def about():
        return View(
            "/about",
            controls=[
                Container(content=Row(controls=[
                    Text("About",style="headlineMedium",color="#FFFFFF",size=20),
                    IconButton(icons.ARROW_BACK,on_click=lambda _: page.go("/")),
                ],alignment=MainAxisAlignment.SPACE_BETWEEN),padding=padding.all(10),
                bgcolor="transparent",
                border_radius=border_radius.all(15),
                margin=margin.all(10)),

                Row(controls=[
                    Image(src="profile.jpg",
                          width=190,
                          height=190)
                ],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[
                    Text(
                "ּ﷽",
                size=100,
                weight=FontWeight.BOLD)],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[Text(
                "This application was developed by me 'Ismail',\n"
                "as a training project to enhance my\nprogramming skills, specifically with\nthe Flet framework.\n"
                "The idea behind this app is to provide a simple\nyet effective tool for converting between\nvarious units of measurement, including length,\nweight, volume, time, and temperature.",
                size=16)],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[Text(
                "Key Features",
                size=18,
                weight=FontWeight.BOLD,
            )],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[Text(
                "- Convert between common units of length,\nsuch as meters, kilometers, and miles.\n"
                "- Supports weight conversions,\nincluding kilograms, pounds, and more.\n"
                "- Easily switch between volume units like\nliters and gallons.\n"
                "- Perform time conversions from\nhours to minutes or seconds.\n"
                "- Includes temperature conversions\nbetween Celsius, Fahrenheit, and Kelvin.\n",
                size=16,
            )],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[Text(
                "How to Use",
                size=18,
                weight=FontWeight.BOLD,
            )],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[Text(
                "1. Enter the value you want to convert.\n"
                "2. Select the unit you're converting\nfrom and the unit you're converting to.\n"
                "3. Click the 'Convert' button to see the result.\n",
                size=16,
            )],alignment=MainAxisAlignment.CENTER),
                
                Row(controls=[
                    Text(
                "This project was inspired by a YouTube channel\ncalled Rakwan, where I learned about\nthe Flet framework.\n"
                "The source code for this application will be\navailable on GitHub as an open-source\nproject, and I hope it can contribute\nto my growing resume and benefit others\nin similar learning journeys.\n"
                "Feel free to use, modify, or contribute\nto this project!",
                size=16)
                ],alignment=MainAxisAlignment.CENTER)
            ],spacing=10,
            scroll=ScrollMode.AUTO
        )


    def unit_converter_page():
        return View(
            "/unit_converter",
            controls=[
                Container(content=Row(controls=[
                    Text("UNIT CONVERTER",style="headlineMedium",color="#FFFFFF",weight="bold",size=30),
                    IconButton(icons.ARROW_BACK,on_click=lambda _: page.go("/")),
                ],alignment=MainAxisAlignment.SPACE_AROUND),padding=padding.all(10),
                bgcolor="transparent",
                border_radius=border_radius.all(15),
                margin=margin.all(10)),

                Row(controls=[
                    Text("\n")
                ]),
                
                Row(controls=[
                    Image(src="unit_converter.png",
                          width=190,
                          height=190)
                ],alignment=MainAxisAlignment.CENTER),

              
                Row(controls=[
                    input_value
                ],alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    from_unit,to_unit
                ],alignment=MainAxisAlignment.CENTER),
    
                Row(controls=[
                    result
                ],alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    convert_button
                ],alignment=MainAxisAlignment.CENTER),

            ]
            )
                
    

    page.on_route_change = change_route
    page.go("/")


    page.update()

app(target=main, assets_dir="assets")