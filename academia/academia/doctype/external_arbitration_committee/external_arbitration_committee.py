# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExternalArbitrationCommittee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		academic_rank: DF.Link | None
		external_faculty: DF.Link | None
		faculty_member: DF.Link | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		university: DF.Link | None
	# end: auto-generated types
	pass
