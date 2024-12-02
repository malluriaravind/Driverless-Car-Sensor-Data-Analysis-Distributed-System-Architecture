from src.data_calculator import DataCalculator
from src.report_generator import ReportGenerator

def main():
    # Initialize calculator and report generator
    calculator = DataCalculator()
    report_gen = ReportGenerator()

    # Calculate data for 10-minute period
    ten_min_data, ten_min_total = calculator.calculate_period_data(10)

    # Calculate data for full route
    full_route_data, route_total = calculator.calculate_period_data(90)

    # Generate report
    report_path = report_gen.generate_report(
        ten_min_data,
        full_route_data,
        ten_min_total,
        route_total
    )

    print(f"Analysis complete! Report generated at: {report_path}")

if __name__ == "__main__":
    main() 