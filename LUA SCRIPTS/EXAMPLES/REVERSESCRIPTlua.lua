-- This script moves a servo if the rover arrives at it's next GPS point.
--
-- The following parameters should be set:
--     SERVO1_FUNCTION = 94 (Script 1) 
local K_SCRIPTING1 = 94
local K_SCRIPTING2 = 95

local K_SCRIPTING5 = 98
local K_SCRIPTING6 = 99
function update()

local CONTROL_OUTPUT_THROTTLE = 3
local CONTROL_OUTPUT_YAW = 4
local steering = vehicle:get_control_output(CONTROL_OUTPUT_YAW)
local throttle = vehicle:get_control_output(CONTROL_OUTPUT_THROTTLE)
--convert from ackerman to skid steering
if (steering and throttle) then
    local summed = steering+throttle
    local diff = throttle-steering
  if(diff>1)then
    diff = 1
  elseif (diff <-1) then
    diff = -1
  end
    
  if(summed>1)then
    summed = 1
  elseif (summed <-1) then
    summed = -1
  end
    

    if(diff<0)then
    SRV_Channels:set_output_norm(K_SCRIPTING5,1)
    SRV_Channels:set_output_norm(K_SCRIPTING1,-diff)
    gcs:send_text(0,"m1 forward")
    else
    SRV_Channels:set_output_norm(K_SCRIPTING5,-1)
    SRV_Channels:set_output_norm(K_SCRIPTING1,diff)
    gcs:send_text(0,"m1 reverse")
    end

    if(summed<0)then
      SRV_Channels:set_output_norm(K_SCRIPTING6,1)
      SRV_Channels:set_output_norm(K_SCRIPTING2,-summed)
      gcs:send_text(0,"m2 forward")

    else 
      SRV_Channels:set_output_norm(K_SCRIPTING6,-1)
      SRV_Channels:set_output_norm(K_SCRIPTING2,summed)
      gcs:send_text(0,"m2 reverse")

    end
  --end of convert steering

  return update, 10 -- run at 100hz
end



end
gcs:send_text(6, "Paint spray script is running")
return update()

