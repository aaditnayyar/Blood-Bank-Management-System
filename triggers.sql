-- Trigger to change the status of a unit in inventory to Transfused whenever a new record is inserted in Transfusion table
DELIMITER //
CREATE TRIGGER update_inventory_status
AFTER INSERT
ON Transfusion FOR EACH ROW
BEGIN
  UPDATE Inventory
  SET Status = 'transfused'
  WHERE ID = NEW.Unit_Id ;
END //
DELIMITER ;