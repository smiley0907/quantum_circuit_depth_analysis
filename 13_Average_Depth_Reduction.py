# 13: Calculate average depth reduction

average_reduction = comparison_df["Depth Reduction (%)"].mean()

print(
    f"Average Circuit Depth Reduction: "
    f"{average_reduction:.2f}%"
)
