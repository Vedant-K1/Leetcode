class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        supply_set = set(supplies)  # Convert supplies list to a set for quick lookup
        result = []  # List to store the recipes that can be made
        changed = True  # Flag to check if any new recipe is made in an iteration

        # Continue until no new recipes can be made
        while changed:
            changed = False  # Reset flag for each iteration
            
            for i in range(len(recipes)):  
                # Skip if the recipe is already available (made in a previous iteration)
                if recipes[i] in supply_set:
                    continue  
                
                # Check if all ingredients for the recipe are available in supply_set
                can_make = True  
                for ing in ingredients[i]:
                    if ing not in supply_set:  # If any ingredient is missing, we can't make it
                        can_make = False  
                        break  

                # If we can make the recipe, add it to the list and mark it as available
                if can_make:
                    result.append(recipes[i])
                    supply_set.add(recipes[i])  # Treat this recipe as a new supply
                    changed = True  # Set flag to indicate we made progress

        return result  # Return the list of recipes that can be made