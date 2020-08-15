<template>
    <nav>
        <v-app-bar flat app>
            <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase indigo--text">
                <span class="font-weight-light">data</span>
                <span>Camp</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-text-field label="통합검색" single-line></v-text-field>
            <v-btn icon @click="onSubmit">
                <v-icon>mdi-magnify</v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer app v-model="drawer" class="primary">
            <v-list>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-item-action>
                        <v-icon class="white--text">{{ link.icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav> 
</template>

<script>
export default {
    props: {
        submit: {
            type: Function,
            default: () => {}
        }
    },
    data() {
        return {
            drawer: false,
            links: [
                { icon: 'mdi-view-dashboard', text: 'Dashboard', route: '/' },
                { icon: 'mdi-movie-open', text: 'Movie', route: '/movie' },
                { icon: 'mdi-account', text: 'User', route: '/user' },
            ]
        }
    },
    methods: {
        onSubmit: function() {
            const params = {
            title: this.title,
            };
        this.submit(params);
        }
    } 
}
</script>