# Inventory

## Airtable

I keep my inventory in Airtable, and use that as a form of system of record.
This is decomposed into a few different things: Inventory, Orders, and
PBS. In addition, I have dedicated tables for 3D printer filament and Brother
TZe cartridges.

### Inventory Table

| Column                     | Type       | Description                                                                                          |
| -------------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| Inventory Number           | Calculated | This is calculated from other fields, including an auto-increment number.                            |
| Category                   | Select     | I group my inventory into "Parts", "Tools", and "Consumables"                                        |
| Manufacturer               | Select     | In most cases, I care about the manufacturer, but others, like passives, it might not matter much.   |
| Manufacturer Part Number   | String     | The manufacturer's part number for reference.                                                        |
| Type                       | Select     | What kind of thing is it (IC, resistor, diode, etc.)                                                 |
| Subtype                    | Select     | For most things, there are subtypes. For resistors it might be metal film or carbon film.            |
| Mount Style                | Select     | This is either traditional through hole (THT) or surface mount (SMD)                                 |
| Value                      | String     | Where it makes sense, like a resistor, the value (e.g., 2k)                                          |
| Rating                     | String     | The rating of the device (e.g, 1/4W for resistor)                                                    |
| Tolerance                  | String     | The tolerance of the device (e.g., 5%)                                                               |
| Package                    | String     | What kind of package is it in. This might just be simple like axial, PDIP-8, or SMD like QFP24.      |
| Description                | String     | A description, typically taken from either the manufacturer or distributor.                          |
| Quantity (purchased)       | Number     | How many of these things have I bought                                                               |
| Quantity (used)            | Number     | How many have I used. This is calculated based on usage in the PBS table.                            |
| Line Item Cost             | Money      | How much did the device cost me, on average, based on the Orders and weighted quantities             |
| Unit Cost (1)              | Money      | What's the latest single-unit pricing for the item.                                                  |
| Unit Cost (bulk)           | Money      | What's the latest bulk pricing for the item. This may be 10, 100, or 1,0000 depending on the device. |
| Loaded Item Cost           | Money      | Calculated from the Orders and allocated shipping costs.                                             |
| Orders                     | Link       | Link to all Orders that had this part in it.                                                         |
| Storage Location           | String     | Where is it located? (e.g., Cabinet 1, Drawer 2)                                                     |
| Total Remaining (Purchase) | Money      | Total value of the remaining inventory based on purchase price.                                      |
| Total Remaining (1)        | Money      | Total value of the remaining inventory based on single-unit costs.                                   |
| Total Remaining (bulk)     | Money      | Total value of the remaining inventory based on bulk purchase.                                       |
| PBS Usage                  | Link       | Linkage to PBS where this is used. |


### Orders

| Column              | Type       | Description                                     |
| ------------------- | ---------- | ----------------------------------------------- |
| Order ID            | Calculated | A sequential order number for internal use.     |
| Vendor              | Select     | Where this order was made.                      |
| Vendor Order Number | String     | Reference to the vendor's system.               |
| Order Cost          | Money      | Total cost of the order                         |
| Order Freight       | Money      | Cost of shipping                                |
| Date Ordered        | Date       | Date the order was submitted                    |
| Date In             | Date       | Date the order was received                     |
| Lag                 | Number     | Number of days between Date Ordered and Date In |


### PBS

| Column         | Type       | Description                                                                                                                                                                     |
| -------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PBS ID         | Calculated | The PBS ID of this item                                                                                                                                                         |
| Project ID     | Link       | Link to the project this PBS item is for. This is used in calculating the PBS ID                                                                                                |
| Project Name   | Link       | Name of the project from the Project table.                                                                                                                                     |
| Name           | String     | Name of this component in the PBS.                                                                                                                                              |
| Type           | Select     | What kind of thing is this? Options are Assembly, Part (meaning purchased), or Designed Part                                                                                    |
| Composition    | Link       | Link to other PBS items that compose into this Assembly. Not used otherwise.                                                                                                    |
| Parts          | Link       | Link to the parts that are used in this item.                                                                                                                                   |
| Revision       | Number     | Current revision of this item.                                                                                                                                                  |
| Quantity       | Number     | Number needed per single product.                                                                                                                                               |
| Build Strategy | Select     | How is this going to be satisfied? Options include Assembly, Off-the-Shelf, 3D Printed, Third-Party Manufacturer, and Undecided.                                                |
| Source         | String     | Source if it's coming from outside.                                                                                                                                             |
| Status         | Select     | Where is this in the design cycle? Options include Not Designed, Design in Progress, Designed, Needs Rework, Ready to Order, Ordered, Received, Completed, Assembled, Cancelled |
| Comments       | String     | Just whatever else needs to be said. |

### Filament

| Column          | Type       | Description                                                                                |
| --------------- | ---------- | ------------------------------------------------------------------------------------------ |
| Part Number     | Calculated | A calculated [part number](part-numbers.md)                                                |
| Brand           | Select     | Who manufactured the filament.                                                             |
| Type            | Select     | PLA, ABS, PETG, etc.                                                                       |
| Diameter        | Number     | Diameter in mm                                                                             |
| Color           | String     | Formal name of the color                                                                   |
| Color (hex)     | String     | CSS-style hex color representation. Useful for using in modeling to get a good appearance. |
| Original Weight | Number     | Weight of the original spool in grams.                                                     |
| Source          | Select     | Where was it purchased from?                                                               |
| Cost            | Money      | How much did the spool cost?                                                               |
| $/g             | Calculated | How much does each gram cost?                                                              |
| Date Purchased  | Date       | When was it purchased?                                                                     |
| Date In         | Date       | When was it received?                                                                      |
| Status          | Select     | One of Ordered, Shipped, In Stock, Out of Stock                                            |
| Location        | String     | Where is this stored in the dry boxes?                                                     |
| Rating          | Stars      | How much do I like this filament?                                                          |
| Notes           | String     | Open ended comments                                                                        |
| Nozzle (C)      | Number     | Temperature recommended for the nozzle                                                     |
| Bed (C)         | Number     | Temperature recommended for the bed                                                        |
| Z (mm)          | Number     | Any specific Z-height needed for optimal extrusion.                                        |


### P-Touch TZe Cartridges

| Column      | Type       | Description                                                                                                           |
| ----------- | ---------- | --------------------------------------------------------------------------------------------------------------------- |
| Part Number | Calculated | A calculated part number                                                                                              |
| Brand       | Select     | Who made this? Important since I use a lot of third-party cartridges.                                                 |
| Type        | Select     | What kind of tape is in the cartridge? For example, Regular, heat shrink tubing, security-tape, extra-astrength, etc. |
| Foreground  | Select     | Print color                                                                                                           |
| Background  | Select     | Background color                                                                                                      |
| Width (mm)  | Select     | How wide is the tape? Typically 6, 9, 12, 18, or 24mm                                                                 |
| Length (mm) | Select     | Length of the tape. Most are 8m.                                                                                      |
| Source      | Select     | Where was it purchased                                                                                                |
| Cost (each) | Money      | How much did a single cartridge cost?                                                                                 |
| $/cm        | Calculated | Calculated cost of a single cm of tape                                                                                |
| Status      | Select     | Ordered, Shipped, In Stock, Out of Stock                                                                              |
| Notes       | String     | Open ended comments |