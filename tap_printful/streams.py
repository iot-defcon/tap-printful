"""Stream type classes for tap-printful."""

from singer_sdk.typing import PropertiesList, IntegerType, StringType, ObjectType, ArrayType, BooleanType, Property
from tap_printful.client import printfulStream


class OrdersStream(printfulStream):
    name = "orders"
    path = "/orders"
    primary_keys = ["id"]
    replication_key = None
    schema = PropertiesList(
        Property("id", IntegerType),
        Property("external_id", StringType),
        Property("store", IntegerType),
        Property("status", StringType),
        Property("shipping", StringType),
        Property("created", IntegerType),
        Property("updated", IntegerType),
        Property("recipient", ObjectType(
            Property("name", StringType),
            Property("company", StringType),
            Property("address1", StringType),
            Property("address2", StringType),
            Property("city", StringType),
            Property("state_code", StringType),
            Property("state_name", StringType),
            Property("country_code", StringType),
            Property("country_name", StringType),
            Property("zip", StringType),
            Property("phone", StringType),
            Property("email", StringType)
        )),
        Property("items", ArrayType(
            ObjectType(
                Property("id", IntegerType),
                Property("external_id", StringType),
                Property("variant_id", IntegerType),
                Property("sync_variant_id", IntegerType),
                Property("external_variant_id", StringType),
                Property("warehouse_product_variant_id", IntegerType),
                Property("quantity", IntegerType),
                Property("price", StringType),
                Property("retail_price", StringType),
                Property("name", StringType),
                Property("product", ObjectType(
                    Property("variant_id", IntegerType),
                    Property("product_id", IntegerType),
                    Property("image", StringType),
                    Property("name", StringType)
                )),
                Property("files", ArrayType(
                    ObjectType(
                        Property("id", IntegerType),
                        Property("type", StringType),
                        Property("hash", StringType),
                        Property("url", StringType),
                        Property("filename", StringType),
                        Property("mime_type", StringType),
                        Property("size", IntegerType),
                        Property("width", IntegerType),
                        Property("height", IntegerType),
                        Property("dpi", IntegerType),
                        Property("status", StringType),
                        Property("created", IntegerType),
                        Property("thumbnail_url", StringType),
                        Property("preview_url", StringType),
                        Property("visible", BooleanType),
                        Property("options", ArrayType(
                            ObjectType(
                                Property("id", StringType),
                                Property("value", StringType)
                            )
                        )),
                    )
                )),
                Property("options", ArrayType(
                    ObjectType(
                        Property("id", StringType),
                        Property("value", StringType)
                    )
                )),
                Property("sku", StringType)
            )
        )),
        Property("incomplete_items", ArrayType(
            ObjectType(
                Property("name", StringType),
                Property("quantity", IntegerType),
                Property("sync_variant_id", IntegerType),
                Property("external_variant_id", StringType),
                Property("external_line_item_id", StringType)
            )
        )),
        Property("costs", ArrayType(
            ObjectType(
                Property("currency", StringType),
                Property("subtotal", StringType),
                Property("discount", StringType),
                Property("shipping", StringType),
                Property("digitiazation", StringType),
                Property("tax", StringType),
                Property("vat", StringType),
                Property("total", StringType),
            )
        )),
        Property("retail_costs", ArrayType(
            ObjectType(
                Property("currency", StringType),
                Property("subtotal", StringType),
                Property("discount", StringType),
                Property("shipping", StringType),
                Property("digitiazation", StringType),
                Property("tax", StringType),
                Property("vat", StringType),
                Property("total", StringType),
            )
        )),
        Property("pricing_breakdown", ArrayType(StringType)),
        Property("shipments", ArrayType(
            ObjectType(
                Property("id", IntegerType),
                Property("carrier", StringType),
                Property("service", StringType),
                Property("tracking_number", StringType),
                Property("tracking_url", StringType),
                Property("created", IntegerType),
                Property("ship_date", StringType),
                Property("shipped_at", IntegerType),
                Property("reshipment", BooleanType),
                Property("items", ArrayType(
                    ObjectType(
                        Property("item_id", IntegerType),
                        Property("quantity", IntegerType),
                    )
                )),
            )
        )),
        Property("gift", ObjectType(
            Property("subject", StringType),
            Property("quantity", StringType),
        )),
        Property("packing_slip", ObjectType(
            Property("email", StringType),
            Property("phone", StringType),
            Property("message", StringType),
            Property("logo_url", StringType),
        )),
    ).to_dict()