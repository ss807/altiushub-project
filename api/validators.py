class Validators:
    def validate_invoice_item(invoice_item_json):
        amount = float(invoice_item_json.get('amount', 0))
        quantity = float(invoice_item_json.get('quantity', 0))
        price = float(invoice_item_json.get('price', 0))
        return amount == quantity * price

    def validate_bill_sundry(bill_sundry_json):
        try:
            amount = float(bill_sundry_json.get('amount', 0))
        except:
            return False
        return True
    
    def validate_invoice(invoice_json):
        total_amount = float(invoice_json.get('total_amount', 0))
        # bill_sundry_amount =
                