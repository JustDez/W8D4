class Cart {
    private shoppingList: { [item: string]: number } = {};

    add_item(item: string, quantity: number): void {
        this.shoppingList[item] = (this.shoppingList[item] || 0) + quantity;
    }

    remove_item(item: string, quantity: number): void {
        if (item in this.shoppingList) {
            if (this.shoppingList[item] <= quantity) {
                delete this.shoppingList[item];
            } else {
                this.shoppingList[item] -= quantity;
            }
        }
    }

    view_list(): void {
        console.log("Shopping List:");
        for (const [item, quantity] of Object.entries(this.shoppingList)) {
            console.log(`${item}: ${quantity}`);
        }
    }

    print_and_quit(): void {
        this.view_list();
        console.log("Goodbye!");
        process.exit();
    }

    run(): void {
        while (true) {
            console.log("Options:");
            console.log("Add");
            console.log("Remove");
            console.log("View");
            console.log("Quit");

            const choice: string = prompt("Enter your choice (Add, Remove, View, Quit): ") || "";

            if (choice === "Add") {
                const item: string = prompt("Enter the item to add: ") || "";
                const quantity: number = parseInt(prompt("Enter the quantity: ") || "0", 10);
                this.add_item(item, quantity);
            } else if (choice === "Remove") {
                const item: string = prompt("Enter the item to remove: ") || "";
                const quantity: number = parseInt(prompt("Enter the quantity to remove: ") || "0", 10);
                this.remove_item(item, quantity);
            } else if (choice === "View") {
                this.view_list();
            } else if (choice === "Quit") {
                this.print_and_quit();
            } else {
                console.log("Invalid choice. Please choose Add, Remove, View, Quit.");
            }
        }
    }
}

// Entry point
if (require.main === module) {
    const shoppingCart = new Cart();
    shoppingCart.run();
}

    