"""Operations functions module"""


def invoice_tax(cost_total, tax_number):
    return (cost_total * tax_number) / 100


def total_sum(cost, current_value):
    return cost + current_value


print(
    f"📜 The total sum is: {total_sum(1, 2)} con el impuesto de {invoice_tax(total_sum(1, 2), 14)}"
)
