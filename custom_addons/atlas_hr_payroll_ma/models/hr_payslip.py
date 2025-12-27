
from odoo import models, fields, api

class AtlasHrPayslip(models.Model):
    _name = 'atlas.hr.payslip'
    _description = 'Bulletin de Paie Atlas (Maroc)'

    name = fields.Char(string="Référence", compute="_compute_name", store=True)
    employee_id = fields.Many2one('hr.employee', string="Employé", required=True)
    date_from = fields.Date(string="Période du", required=True)
    date_to = fields.Date(string="Période au", required=True)
    
    # Montants
    base_salary = fields.Float(string="Salaire de Base", required=True)
    other_taxable = fields.Float(string="Autres Primes Imposables", default=0.0)
    gross_salary = fields.Float(string="Salaire Brut", compute="_compute_gross", store=True)
    
    # Cotisations
    cnss_rate = fields.Float(string="Taux CNSS (%)", default=4.48)
    cnss_amount = fields.Float(string="Montant CNSS", compute="_compute_deductions", store=True)
    
    amo_rate = fields.Float(string="Taux AMO (%)", default=2.26)
    amo_amount = fields.Float(string="Montant AMO", compute="_compute_deductions", store=True)
    
    # IR
    taxable_income = fields.Float(string="Net Imposable", compute="_compute_deductions", store=True)
    ir_amount = fields.Float(string="IR", compute="_compute_ir", store=True)
    
    net_salary = fields.Float(string="Salaire Net à Payer", compute="_compute_net", store=True)

    @api.depends('employee_id', 'date_from')
    def _compute_name(self):
        for slip in self:
            if slip.employee_id and slip.date_from:
                slip.name = f"Paie - {slip.employee_id.name} - {slip.date_from.strftime('%m/%Y')}"
            else:
                slip.name = "Nouveau"

    @api.depends('base_salary', 'other_taxable')
    def _compute_gross(self):
        for slip in self:
            slip.gross_salary = (slip.base_salary or 0.0) + (slip.other_taxable or 0.0)

    @api.depends('gross_salary', 'cnss_rate', 'amo_rate')
    def _compute_deductions(self):
        for slip in self:
            gross = slip.gross_salary or 0.0
            slip.cnss_amount = min(gross, 6000.0) * ((slip.cnss_rate or 4.48) / 100.0)
            slip.amo_amount = gross * ((slip.amo_rate or 2.26) / 100.0)
            frais_pro = min(gross * 0.20, 2500.0)
            slip.taxable_income = gross - slip.cnss_amount - slip.amo_amount - frais_pro

    @api.depends('taxable_income')
    def _compute_ir(self):
        for slip in self:
            income = slip.taxable_income or 0.0
            # Barème IR Marocain 2024 simplifié (mensuel)
            if income <= 2500:
                ir = 0
            elif income <= 4166:
                ir = (income * 0.10) - 250
            elif income <= 5000:
                ir = (income * 0.20) - 666
            elif income <= 6666:
                ir = (income * 0.30) - 1166
            elif income <= 15000:
                ir = (income * 0.34) - 1433
            else:
                ir = (income * 0.38) - 2033
            slip.ir_amount = max(ir, 0)

    @api.depends('gross_salary', 'cnss_amount', 'amo_amount', 'ir_amount')
    def _compute_net(self):
        for slip in self:
            gross = slip.gross_salary or 0.0
            cnss = slip.cnss_amount or 0.0
            amo = slip.amo_amount or 0.0
            ir = slip.ir_amount or 0.0
            slip.net_salary = gross - cnss - amo - ir
