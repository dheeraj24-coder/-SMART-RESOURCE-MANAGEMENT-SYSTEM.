# SMART RESOURCE MANAGEMENT SYSTEM
# Using OOP + Functions + Dictionary + List + If Else

class ResourceManagement:

    def __init__(self):

        # Resource Data
        self.resources = [
            {
                "name": "Food",
                "quantity": 500,
                "unit": "kg",
                "threshold": 200
            },

            {
                "name": "Water",
                "quantity": 1000,
                "unit": "liters",
                "threshold": 400
            },

            {
                "name": "Medical Kits",
                "quantity": 150,
                "unit": "boxes",
                "threshold": 50
            },

            {
                "name": "Electricity",
                "quantity": 800,
                "unit": "units",
                "threshold": 300
            }
        ]

    # Show All Resources
    def show_resources(self):

        print("\n===== ALL RESOURCES =====")

        for resource in self.resources:

            print("Name :", resource["name"])
            print("Quantity :", resource["quantity"], resource["unit"])
            print("Threshold :", resource["threshold"])
            print("--------------------------")

    # Add Resource
    def add_resource(self):

        name = input("Enter Resource Name : ")
        quantity = int(input("Enter Quantity : "))

        found = False

        # Check Existing Resource
        for resource in self.resources:

            if resource["name"].lower() == name.lower():

                # Add quantity to existing resource
                resource["quantity"] += quantity

                print("Quantity Added To Existing Resource")

                found = True
                break

        # If resource not found then create new
        if found == False:

            unit = input("Enter Unit : ")
            threshold = int(input("Enter Threshold : "))

            new_resource = {
                "name": name,
                "quantity": quantity,
                "unit": unit,
                "threshold": threshold
            }

            self.resources.append(new_resource)

            print("New Resource Added Successfully")

    # Update Resource
    def update_resource(self):

        name = input("Enter Resource Name To Update : ")

        found = False

        for resource in self.resources:

            if resource["name"].lower() == name.lower():

                new_quantity = int(input("Enter New Quantity : "))

                resource["quantity"] = new_quantity

                print("Resource Updated Successfully")

                found = True
                break

        if found == False:
            print("Resource Not Found")

    # Delete Resource
    def delete_resource(self):

        name = input("Enter Resource Name To Delete : ")

        found = False

        for resource in self.resources:

            if resource["name"].lower() == name.lower():

                self.resources.remove(resource)

                print("Resource Deleted Successfully")

                found = True

                break

        if found == False:
            print("Resource Not Found")

    # Low Stock Alert
    def low_stock_alert(self):

        print("\n===== LOW STOCK ALERT =====")

        alert_found = False

        for resource in self.resources:

            if resource["quantity"] < resource["threshold"]:

                print(resource["name"], "is LOW in stock!")

                print(
                    "Available :",
                    resource["quantity"],
                    resource["unit"]
                )

                alert_found = True

        if alert_found == False:
            print("All Resources Are Sufficient")

    # Usage Report
    def usage_report(self):

        print("\n===== RESOURCE REPORT =====")

        total_resources = len(self.resources)

        print("Total Resources :", total_resources)

        for resource in self.resources:

            print(
                resource["name"],
                "->",
                resource["quantity"],
                resource["unit"]
            )


# Object Create
system = ResourceManagement()


# Main Menu
while True:

    print("\n========== SMART RESOURCE MANAGEMENT SYSTEM ==========")

    print("1. Show Resources")
    print("2. Add Resource")
    print("3. Update Resource")
    print("4. Delete Resource")
    print("5. Low Stock Alert")
    print("6. Usage Report")
    print("7. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        system.show_resources()

    elif choice == "2":
        system.add_resource()

    elif choice == "3":
        system.update_resource()

    elif choice == "4":
        system.delete_resource()

    elif choice == "5":
        system.low_stock_alert()

    elif choice == "6":
        system.usage_report()

    elif choice == "7":
        print("System Closed")
        break

    else:
        print("Invalid Choice")
