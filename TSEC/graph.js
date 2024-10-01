function createTransactionAmountGraph(transactions, chartId) {
    const ctx = document.getElementById(chartId).getContext('2d');
    
    // Group transactions by month and sum the amounts
    const monthlyData = transactions.reduce((acc, t) => {
        const date = new Date(t.date);
        const month = date.getMonth();
        acc[month] = (acc[month] || 0) + t.amount;
        return acc;
    }, {});

    // Prepare data for all 12 months
    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const amounts = monthNames.map((_, index) => monthlyData[index] || 0);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: monthNames,
            datasets: [{
                label: 'Transaction Amount',
                data: amounts,
                backgroundColor: '#4285F4',
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Total Amount'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Month'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Monthly Transaction Amounts'
                }
            }
        }
    });
}

function createTransactionTypeGraph(transactions, chartId) {
    const ctx = document.getElementById(chartId).getContext('2d');
    const typeCounts = transactions.reduce((acc, t) => {
        acc[t.type] = (acc[t.type] || 0) + 1;
        return acc;
    }, {});

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(typeCounts),
            datasets: [{
                data: Object.values(typeCounts),
                backgroundColor: ['#4285F4', '#34A853', '#FBBC05', '#EA4335']
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Transaction Types Distribution'
                }
            }
        }
    });
}

function createTransactionTimelineGraph(transactions, chartId) {
    const ctx = document.getElementById(chartId).getContext('2d');
    const timeline = transactions.reduce((acc, t) => {
        const date = t.timestamp.toLocaleDateString();
        acc[date] = (acc[date] || 0) + 1;
        return acc;
    }, {});

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: Object.keys(timeline),
            datasets: [{
                label: 'Number of Transactions',
                data: Object.values(timeline),
                borderColor: '#4285F4',
                tension: 0.1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Transactions'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Date'
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Transaction Timeline'
                }
            }
        }
    });
}

function createBarGraph(canvasId, data, options) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    if (window[canvasId + 'Chart']) {
        window[canvasId + 'Chart'].destroy();
    }
    window[canvasId + 'Chart'] = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: options
    });
}
