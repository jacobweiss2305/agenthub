from swarm import Bee


def process_refund(item_id, reason="NOT SPECIFIED"):
    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before processing the refund."""
    print(f"[mock] Refunding item {item_id} because {reason}...")
    return "Success!"


def apply_discount():
    """Apply a discount to the user's cart."""
    print("[mock] Applying discount...")
    return "Applied discount of 11%"


triage_bee = Bee(
    name="Triage Bee",
    instructions="Determine which bee is best suited to handle the user's request, and transfer the conversation to that bee.",
)
sales_bee = Bee(
    name="Sales Bee",
    instructions="Be super enthusiastic about selling bees.",
)
refunds_bee = Bee(
    name="Refunds Bee",
    instructions="Help the user with a refund. If the reason is that it was too expensive, offer the user a refund code. If they insist, then process the refund.",
    functions=[process_refund, apply_discount],
)


def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current bee."""
    return triage_bee


def transfer_to_sales():
    return sales_bee


def transfer_to_refunds():
    return refunds_bee


triage_bee.functions = [transfer_to_sales, transfer_to_refunds]
sales_bee.functions.append(transfer_back_to_triage)
refunds_bee.functions.append(transfer_back_to_triage)
