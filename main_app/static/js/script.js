const dateEl = document.getElementById("id_date");
const checkboxEl = document.getElementById("id_fertilized");

M.Datepicker.init(dateEl, {
  format: "yyyy-mm-dd",
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true,
});
