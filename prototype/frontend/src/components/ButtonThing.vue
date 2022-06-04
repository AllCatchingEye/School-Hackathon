<template>
    <button v-bind="$attrs" class="button is-warning"> {{ buttonText }} </button>
</template>

<script>
export default {
    props: {
        buttonText: {
            type: String,
            default: () => "<ButtonName>",
        }
    }
};
</script>


<style scoped>
</style>