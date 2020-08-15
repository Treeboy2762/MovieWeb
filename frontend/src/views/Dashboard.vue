<template>
  <div class="dashboard">
    <h1 class="subheading">Movie Rating Database</h1>
    <v-container class="my-1 mx-1 grey--text">
      <v-card flat class="pa-3">
        <v-layout row wrap>
          <v-flex xs12 md6>
            <div class="caption grey--text">Project Title</div>
            <div>Create a new website</div>
          </v-flex>   
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Person</div>
            <div>dataCamp test</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Due by</div>
            <div>9 Aug 2020</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
            <div class="caption grey--text">Status</div>
            <div>Complete</div>
          </v-flex>
        </v-layout>
      </v-card>

    </v-container>  
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {

  }
}
</script>