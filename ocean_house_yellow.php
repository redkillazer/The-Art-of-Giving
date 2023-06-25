<?php

// Define function to donate to an organization 
function donate($organization, $amount)
{
    // Check if donation amount is valid
    if($amount > 0)
    {
        // If valid, add to charity's donations
        $donations = $organization['donations'] + $amount;
        $organization['donations'] = $donations;
    }
    else
    {
        // Otherwise, show error
        echo "Cannot donate less than or equal to 0<br/>";
    }
    
    // Return updated donation info
    return $organization;
}

// Define function to sum donations
function sum_donations($organizations)
{
    // Initialize sum
    $sum = 0;
    
    // Loop through all donations
    foreach($organizations as $organization)
    {
        // Add to running sum
        $sum += $organization['donations'];
    }
    
    // Return total donations
    return $sum;
}

// Define function to print donations
function print_donations($organizations)
{
    // Loop through all donations
    foreach($organizations as $organization)
    {
        // Print donation info
        echo "Donated " . $organization['donations'] . " to " . $organization['name'] . "<br/>";
    }
}

// Define function to get donation info
function get_donation_info($organization_name)
{
    // Create array to hold donation info
    $organization = array();
    
    // Set organization name
    $organization['name'] = $organization_name;
    
    // Initialize donations to 0
    $organization['donations'] = 0;
    
    // Return donation info
    return $organization;
}

// Define function to give to multiple organizations
function give_to_multiple($organizations, $amount)
{
    // Loop through all organizations
    foreach($organizations as $organization)
    {
        // Get updated donation info
        $organization = donate($organization, $amount);
    }
    
    // Return updated donation info
    return $organizations;
}

// Get donation info for 5 organizations
$organization1 = get_donation_info("Organization1");
$organization2 = get_donation_info("Organization2");
$organization3 = get_donation_info("Organization3");
$organization4 = get_donation_info("Organization4");
$organization5 = get_donation_info("Organization5");

// Put all donation info into an array
$organizations = array($organization1, $organization2, $organization3, $organization4, $organization5);

// Donate $100 to the first organization
$organization1 = donate($organization1, 100);

// Donate $50 to all other organizations
$organizations = give_to_multiple($organizations, 50);

// Get total donations
$total_donations = sum_donations($organizations);

// Print statements for each donation
print_donations($organizations);

// Print total donations
echo "Total donations: " . $total_donations;

?>