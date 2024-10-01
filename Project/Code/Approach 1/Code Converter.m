
function length_conversion()
    units = {'meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'};
    conversion_to_meters = containers.Map(units, [1, 1000, 0.01, 0.001, 1609.34, 0.9144, 0.3048, 0.0254]);
    
    while true
        fprintf('\nLength Conversion\n');
        disp('Available units: meters, kilometers, centimeters, millimeters, miles, yards, feet, inches');
        
        try
            value = input('Enter the value to convert: ');
            from_unit = lower(input('Enter the unit to convert from: ', 's'));
            to_unit = lower(input('Enter the unit to convert to: ', 's'));
            
            if ~isKey(conversion_to_meters, from_unit) || ~isKey(conversion_to_meters, to_unit)
                disp('Invalid units. Please try again.');
                continue;
            end
            
            result = convert_length(value, from_unit, to_unit, conversion_to_meters);
            
            if ~isempty(result)
                fprintf('%f %s is equal to %f %s\n', value, from_unit, result, to_unit);
            else
                disp('Conversion error. Please check your units and try again.');
            end
            
            another_conversion = lower(input('Do you want to perform another conversion? (yes/no): ', 's'));
            if ~strcmp(another_conversion, 'yes')
                disp('Exiting the program. Goodbye!');
                break;
            end
            
        catch ME
            disp('Invalid input. Please enter numerical values.');
        end
    end
end

function converted_value = convert_length(value, from_unit, to_unit, conversion_to_meters)
    % Convert from the initial unit to meters
    value_in_meters = value * conversion_to_meters(from_unit);
    
    % Convert from meters to the target unit
    converted_value = value_in_meters / conversion_to_meters(to_unit);
end

% Call the main function to start the program
length_conversion();
