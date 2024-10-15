# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UniversityAcademicCalendar(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from academia.academia.doctype.academic_calender__procedure.academic_calender__procedure import AcademicCalenderProcedure
		from frappe.types import DF

		academic_calendar_term_one: DF.Table[AcademicCalenderProcedure]
		academic_calendar_term_three: DF.Table[AcademicCalenderProcedure]
		academic_calendar_term_two: DF.Table[AcademicCalenderProcedure]
		academic_term_one: DF.Data
		academic_term_three: DF.Data | None
		academic_term_two: DF.Data | None
		academic_year: DF.Data
		is_hour_system: DF.Check
		master_academic_calendar: DF.Table[AcademicCalenderProcedure]
		master_academic_year: DF.Data | None
	# end: auto-generated types
	pass
