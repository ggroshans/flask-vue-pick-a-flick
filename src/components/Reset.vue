<template>
  <div>
    <b-button id="tooltip-reset-searches" variant="danger" @click="deleteSearchesPrelim"
      >Reset Searches</b-button
    >
    <b-tooltip target="tooltip-reset-searches" triggers="hover">
      Resets only previously swiped movies and past searches! Your matches will remain saved.
    </b-tooltip>
    <b-button id="tooltip-reset-everything" variant="danger" @click="deleteEverythingPrelim"
      >Reset Everything</b-button
    >
    <b-tooltip target="tooltip-reset-everything" triggers="hover">
      Resets previously swiped movies, past searches and your matched movie list!
    </b-tooltip>

    <b-modal
      id="reset-modal"
      title="BootstrapVue"
      header-bg-variant="danger"
      header-text-variant="light"
      size="sm"
    >
      <div class="delete-modal-title" slot="modal-title">
        <strong>Delete Confirmation</strong>
      </div>
      <p v-if="deleteSearches" class="my-4">
        Are you sure you want to reset<br />
        <strong>all searches</strong> ?
      </p>
      <p v-if="deleteEverything" class="my-4">
        Are you sure you want to reset<br />
        <strong>everything</strong> ?
      </p>

      <div slot="modal-footer">
        <b-button @click="closeModal" button-size="sm">Cancel</b-button>
        <b-button
          v-if="deleteSearches"
          @click="deleteSearchesFinal"
          class="btn btn-danger"
          button-size="sm"
          >Delete Searches</b-button
        >
        <b-button
          v-if="deleteEverything"
          @click="deleteEverythingFinal"
          class="btn btn-danger"
          button-size="sm"
          >Delete Everything</b-button
        >
      </div>
    </b-modal>
  </div>
</template>

<script>
import requestPath from '../fetchUtility';
export default {
  data() {
    return {
      deleteSearches: false,
      deleteEverything: false
    };
  },
  methods: {
    deleteSearchesPrelim() {
      this.deleteEverything = false;
      this.deleteSearches = true;
      this.$root.$emit("bv::show::modal", "reset-modal");
    },
    deleteEverythingPrelim() {
      this.deleteSearches = false;
      this.deleteEverything = true;
      this.$root.$emit("bv::show::modal", "reset-modal");
    },
    async deleteSearchesFinal() {
      this.deleteEverything = false;
      this.deleteSearches = false;
      let resp = await fetch(requestPath("delete_searches"), {
        method: "DELETE",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        }
      });
      this.$root.$emit("bv::hide::modal", "reset-modal");
    },
    async deleteEverythingFinal() {
      this.deleteSearches = false;
      this.deleteEverything = false;
      this.$root.$emit("bv::hide::modal", "reset-modal");
      let resp = await fetch(requestPath("delete_everything"), {
        method: "DELETE",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-TOKEN": $cookies.get("csrf_access_token")
        }
      });
      this.$store.commit("setUserMovieList", []);
    },
    closeModal() {
      this.$root.$emit("bv::hide::modal", "reset-modal");
    }
  },
  created() {}
};
</script>

<style scoped></style>
