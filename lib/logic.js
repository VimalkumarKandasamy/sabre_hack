/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';
/**
 * Write your transction processor functions here
 */

/**
 * Sample transaction
 * @param {org.sabre.hack.Update_readings} ur
 * @transaction
 */


async function Update_readings(ur) {
    let assetReg = await getAssetRegistry('org.sabre.hack.Vehicle');

    ur.vehicle.tyre_pressure = ur.tyre_pressure;
    ur.vehicle.oil_status = ur.oil_status;
    ur.vehicle.fuel_status = ur.fuel_status;

    await assetReg.update(ur.vehicle);

  }








  /**
 * Sample transaction
 * @param {org.sabre.hack.Update_maintenance} um
 * @transaction
 */


async function Update_maintenance(um) {
    let assetReg = await getAssetRegistry('org.sabre.hack.Vehicle');


    um.vehicle.last_serviced_date = um.serviced_date;
    
    await assetReg.update(um.vehicle);
  }


    /**
 * Sample transaction
 * @param {org.sabre.hack.Update_insurance} ui
 * @transaction
 */


async function Update_insurance(ui) {
    let assetReg = await getAssetRegistry('org.sabre.hack.Vehicle');


    ui.vehicle.insurance_validity = ui.insurance_validity;
    
    await assetReg.update(ui.vehicle);
  }
  

      /**
 * Sample transaction
 * @param {org.sabre.hack.Update_trip} ut
 * @transaction
 */


async function Update_trip(ut) {
    let assetReg = await getAssetRegistry('org.sabre.hack.Vehicle');
    let participantReg = await getParticipantRegistry('org.sabre.hack.Driver');

    let old_km= ut.vehicle.km_driven;
    ut.vehicle.km_driven = ut.km_travelled + old_km ;
    
    await assetReg.update(ut.vehicle);
    await participantReg.update(ut.driver);
  }
