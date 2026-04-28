// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({

  devtools: { enabled: true },

   srcDir: 'app',

  modules: ['@nuxt/image', '@nuxt/icon', '@nuxtjs/tailwindcss','@pinia/nuxt','@nuxtjs/google-fonts',],
  css: ['~/assets/scss/main.scss'],

    googleFonts: {
      families: {
        'DM Sans': [400, 500, 600, 700, 800],
        'JetBrains Mono': [400, 600],
      },
      display: 'swap',
      preload: true,
    },

    app: {
      head: {
        title: 'AgriSense',
        meta: [
          { charset: 'utf-8' },
          {
            name: 'viewport',
            content: 'width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1, user-scalable=no',
          },
          { name: 'description', content: 'Application agricole connectée — météo, capteurs, santé des cultures' },
          { name: 'theme-color', content: '#1a1a1a' },
          { name: 'apple-mobile-web-app-capable', content: 'yes' },
          { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' },
          { name: 'apple-mobile-web-app-title', content: 'AgriSense' },
        ],
        link: [
          { rel: 'apple-touch-icon', href: '/icon-192.png' },
        ],
      },
      pageTransition: { name: 'page', mode: 'out-in' },
    },

    vite: {
      css: {
        preprocessorOptions: {
          scss: {
            // No global additionalData needed — main.scss is loaded via css[]
          },
        },
      },
    },

    // SSR off for mobile-first PWA feel
    ssr: false,

    imports: {
        autoImport: true,
      },

    compatibilityDate: '2024-11-01',
})