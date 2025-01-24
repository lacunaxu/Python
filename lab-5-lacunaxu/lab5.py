import csv
from typing import Any, Dict, List, Tuple


def analyze_employee_data(filepath: str) -> Tuple[int, dict, str, List[Tuple[float, str]]]:
    
    employees_num = 0
    employees_by_gender = {'Male': 0, 'Female': 0}
    joblevel_count = {}
    highest_male = []
    highest_female = []
    
    with open(filepath, 'r') as file_handle:
        data = csv.DictReader(file_handle)
        
        for line in data:
            employees_num += 1
            
            gender = line['Gender']
            job_level = line['JobLevel']
            
            if gender in employees_by_gender:
                employees_by_gender[gender] += 1
            
            if job_level in joblevel_count:
                joblevel_count[job_level] += 1
            else:
                joblevel_count[job_level] = 1
                
            problem_solving_score = float(line['ProblemSolvingScore'])
            
            if gender == 'Male':
                highest_male.append(problem_solving_score)
            else:
                highest_female.append(problem_solving_score)
        
        performance_by_employee = [
            (max(highest_male), 'Male'),
            (max(highest_female), 'Female')
        ]
        
        highest_ps_list = sorted(performance_by_employee)
        common_joblevel = max(joblevel_count, key=joblevel_count.get)
    
    return employees_num, employees_by_gender, common_joblevel, highest_ps_list


def analyze_sales_data(filepath: str) -> Tuple[Dict[str, int], Dict[str, float], float, List[str]]:
    sales_by_productcategory = {}
    salesregion_amounts = {}
    salesregion_counts = {}
    id_collect = []
    saleamount_collect = []

    with open(filepath, 'r') as file_handle:
        data = csv.DictReader(file_handle)

        for line in data:

            product_category = line['ProductCategory']
            if product_category in sales_by_productcategory:
                sales_by_productcategory[product_category] += 1
            else:
                sales_by_productcategory[product_category] = 1

            sales_region = line['SalesRegion']
            sale_amount = float(line['SaleAmount'])
            if sales_region in salesregion_amounts:
                salesregion_amounts[sales_region] += sale_amount
                salesregion_counts[sales_region] += 1
            else:
                salesregion_amounts[sales_region] = sale_amount
                salesregion_counts[sales_region] = 1

            product_id = line['ProductID']
            id_collect.append(product_id)
            saleamount_collect.append(sale_amount)

    max_saleamount = max(saleamount_collect)
    highest_productid = [id_collect[i] for i in range(len(saleamount_collect)) if saleamount_collect[i] == max_saleamount]

    salesregion_avg = {region: round(salesregion_amounts[region] / salesregion_counts[region], 2) for region in salesregion_amounts}

    return sales_by_productcategory, salesregion_avg, max_saleamount, highest_productid


def analyze_bank_data(filepath: str) -> Dict[str, Any]:

    deposit_list = set()
    withdrawal_list = set()
    
    with open(filepath, 'r') as file_handle:
        data = csv.DictReader(file_handle)
                                
        for line in data:
            transaction_type = line['TransactionType']
            transaction_description = line['TransactionDescription']

            if transaction_type == "Deposit":
                deposit_list.add(transaction_description)
            elif transaction_type == "Withdrawal":
                withdrawal_list.add(transaction_description)

        common = deposit_list.intersection(withdrawal_list)

        only_deposit = sorted(list(deposit_list - common))
        only_withdrawal = sorted(list(withdrawal_list - common))
        common = sorted(list(common))
        exclusive_count = len(only_deposit) + len(only_withdrawal)

        return {
            'only_deposit': only_deposit,
            'common': common,
            'only_withdrawal': only_withdrawal,
            'exclusive_count': exclusive_count
        }
        
