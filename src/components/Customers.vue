<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Customers</h1>
        <h6>(Press on a column's entry to sort a specific entry increasingly)</h6>
        <hr>
        <br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.customer-modal>Add Customer</button>
        <button type="button" class="btn btn-primary btn-sm" @click="showChart()" v-b-modal.chart-modal>See chart</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th @click="sort('id')" scope="col">ID</th>
              <th @click="sort('segment')" scope="col">Segment</th>
              <th @click="sort('gender')" scope="col">Gender</th>
              <th @click="sort('years_customer')" scope="col">years_customer</th>
              <th @click="sort('no_of_complaints')" scope="col">no_of_complaints</th>
              <th @click="sort('contract_value')" scope="col">contract_value</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(customer, index) in customers" :key="index">
              <td>{{ customer.id }}</td>
              <td>{{ customer.segment }}</td>
              <td>{{ customer.gender }}</td>
              <td>{{ customer.years_customer }}</td>
              <td>{{ customer.no_of_complaints }}</td>
              <td>{{ customer.contract_value }}</td>
              <td>
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.customer-update-modal
                  @click="editCustomer(customer)"
                >Update</button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteCustomer(customer)"
                >Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal ref="addCustomerModal" id="customer-modal" title="Add a new customer" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-id-group" label="ID:" label-for="form-id-input">
          <b-form-input
            id="form-id-input"
            type="text"
            v-model="addCustomerForm.id"
            required
            placeholder="Enter ID"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-segment-group" label="Segment:" label-for="form-segment-input">
          <b-form-input
            id="form-segment-input"
            type="text"
            v-model="addCustomerForm.segment"
            required
            placeholder="Enter segment"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="form-gender-group" label="Gender:" label-for="form-gender-input">
          <b-form-input
            id="form-gender-input"
            type="text"
            v-model="addCustomerForm.gender"
            required
            placeholder="Enter gender"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-years_customer-group"
          label="Years customer:"
          label-for="form-years_customer-input"
        >
          <b-form-input
            id="form-years_customer-input"
            type="text"
            v-model="addCustomerForm.years_customer"
            required
            placeholder="Enter number of years this customer exists"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-no_of_complaints-group"
          label="Number of complaints:"
          label-for="form-no_of_complaints-input"
        >
          <b-form-input
            id="form-no_of_complaints-input"
            type="text"
            v-model="addCustomerForm.no_of_complaints"
            required
            placeholder="Number of complaints"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-contract_value-group"
          label="Contract value:"
          label-for="form-contract_value-input"
        >
          <b-form-input
            id="form-contract_value-input"
            type="text"
            v-model="addCustomerForm.contract_value"
            required
            placeholder="Contract value"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editCustomerModal" id="customer-update-modal" title="Update" hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-id-edit-group" label="ID:" label-for="form-id-edit-input">
          <b-form-input
            id="form-id-edit-input"
            type="text"
            v-model="editForm.id"
            required
            placeholder="Enter ID"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-segment-edit-group"
          label="Segment:"
          label-for="form-segment-edit-input"
        >
          <b-form-input
            id="form-segment-edit-input"
            type="text"
            v-model="editForm.segment"
            required
            placeholder="Enter segment"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-gender-edit-group"
          label="Gender:"
          label-for="form-gender-edit-input"
        >
          <b-form-input
            id="form-gender-edit-input"
            type="text"
            v-model="editForm.gender"
            required
            placeholder="Enter gender"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-years_customer-edit-group"
          label="Years customer:"
          label-for="form-years_customer-edit-input"
        >
          <b-form-input
            id="form-years_customer-edit-input"
            type="text"
            v-model="editForm.years_customer"
            required
            placeholder="Enter years_customer"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-no_of_complaints-edit-group"
          label="Number of complaints:"
          label-for="form-no_of_complaints-edit-input"
        >
          <b-form-input
            id="form-no_of_complaints-edit-input"
            type="text"
            v-model="editForm.no_of_complaints"
            required
            placeholder="Enter no_of_complaints"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="form-contract_value-edit-group"
          label="Contract value:"
          label-for="form-contract_value-edit-input"
        >
          <b-form-input
            id="form-contract_value-edit-input"
            type="text"
            v-model="editForm.contract_value"
            required
            placeholder="Enter contract_value"
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>

  <b-modal ref="chartModal" id="chart-modal" title="Chart" hide-footer>

    </b-modal>

  </div>
</template>


<script>
import axios from "axios";
import Alert from "./Alert";

export default {
  data() {
    return {
      customers: [],
      chartData: [],
      addCustomerForm: {
        id: "",
        segment: "",
        gender: "",
        years_customer: "",
        no_of_complaints: "",
        contract_value: ""
      },
      message: "",
      showMessage: false,
      editForm: {
        id: "",
        segment: "",
        gender: "",
        years_customer: "",
        no_of_complaints: "",
        contract_value: ""
      }
    };
  },
  components: {
    alert: Alert
  },
  methods: {
    sort(key) {
      const path = "http://localhost:5000/customers";
      axios
        .get(path)
        .then(res => {
          this.customers = res.data.customers.sort( (a,b) => a[key] - b[key]);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    showChart() {
      const path = "http://localhost:5000/customers";
      axios
        .get(path)
        .then(res => {
          this.chartData = res.data.customers;
          
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getCustomers() {
      const path = "http://localhost:5000/customers";
      axios
        .get(path)
        .then(res => {
          this.customers = res.data.customers;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addCustomer(payload) {
      const path = "http://localhost:5000/customers";
      axios
        .post(path, payload)
        .then(() => {
          this.getCustomers();
          this.message = "Customer added!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
          this.getCustomers();
        });
    },
    initForm() {
      this.addCustomerForm.id = "";
      this.addCustomerForm.segment = "";
      this.addCustomerForm.gender = "";
      this.addCustomerForm.years_customer = "";
      this.addCustomerForm.no_of_complaints = "";
      this.addCustomerForm.contract_value = "";
      this.editForm.id = "";
      this.editForm.segment = "";
      this.editForm.gender = "";
      this.editForm.years_customer = "";
      this.editForm.no_of_complaints = "";
      this.editForm.contract_value = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      const payload = {
        id: this.addCustomerForm.id,
        segment: this.addCustomerForm.segment,
        gender: this.addCustomerForm.gender,
        years_customer: this.addCustomerForm.years_customer,
        no_of_complaints: this.addCustomerForm.no_of_complaints,
        contract_value: this.addCustomerForm.contract_value
      };
      this.addCustomer(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addCustomerModal.hide();
      this.initForm();
    },
    editCustomer(customer) {
      this.editForm = customer;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCustomerModal.hide();
      const payload = {
        id: this.editForm.id,
        segment: this.editForm.segment,
        gender: this.editForm.gender,
        years_customer: this.editForm.years_customer,
        no_of_complaints: this.editForm.no_of_complaints,
        contract_value: this.editForm.contract_value
      };
      this.updateCustomer(payload, this.editForm.id);
    },
    updateCustomer(payload, customerID) {
      const path = `http://localhost:5000/customers/${customerID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getCustomers();
          this.message = "Customer updated!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getCustomers();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editCustomerModal.hide();
      this.initForm();
      this.getCustomers(); // why?
    },
    removeCustomer(customerID) {
      const path = `http://localhost:5000/customers/${customerID}`;
      axios
        .delete(path)
        .then(() => {
          this.getCustomers();
          this.message = "Customer removed!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getCustomers();
        });
    },
    onDeleteCustomer(customer) {
      this.removeCustomer(customer.id);
    }
  },
  created() {
    this.getCustomers();
  }
};
</script>